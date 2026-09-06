import json

with open('proyecto_obra.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Room internal dimensions
# X: -124 to 124 (Width = 248)
# Z: -181.25 to 181.25 (Depth = 362.5)
# Y: floor ~0, ceiling ~290

# Let's filter out the old acoustic treatments
new_nodes = []
for node in data['nodes']:
    if node.get('clase') == 'TRATAMIENTO_ACUSTICO':
        continue
    new_nodes.append(node)

# 1. Panel Techo (Lana de Vidrio 240x150)
# We will place it above the speakers and listener without clipping.
# Span Z: from -181 (wall) to -31. Center Z = -106. Depth = 150.
# Width = 240. Center X = 0.
new_nodes.append({
    "id": "panel_techo_principal",
    "layer": "ACUSTICA",
    "clase": "TRATAMIENTO_ACUSTICO",
    "geometry": {
        "type": "BoxGeometry",
        "width": 240,
        "height": 10,
        "depth": 150
    },
    "transform": {
        "position": [0, 275, -106],
        "rotation": [0, 0, 0]
    },
    "material_ref": "panel_acustico_negro",
    "properties": {
        "tipo": "Panel Nube Techo (240x150)"
    }
})

# 2. Trampas de Graves (Bass Traps)
# Since NE and SW corners are blocked by doors, horizontal soffit traps are best.
# We'll put them along the top edges of the North and South walls.
# They will be triangular prisms (CylinderGeometry with 3 sides).
# Length = 248 (fitting exactly between East and West walls).
# Height = 248. Radius = 30.
# We need to rotate them so the flat side is down or diagonally facing the room.
new_nodes.extend([
    {
      "id": "trampa_graves_norte_techo",
      "layer": "ACUSTICA",
      "clase": "TRATAMIENTO_ACUSTICO",
      "geometry": {
        "type": "RightTrianglePrism",
        "width": 40,
        "height": 40,
        "depth": 248
      },
      "transform": {
        "position": [0, 265, -161.25],
        "rotation": [180, 90, 0]
      },
      "material_ref": "espuma_acustica",
      "properties": {
        "tipo": "Trampa Graves Esquinera Norte"
      }
    },
    {
      "id": "trampa_graves_sur_techo",
      "layer": "ACUSTICA",
      "clase": "TRATAMIENTO_ACUSTICO",
      "geometry": {
        "type": "RightTrianglePrism",
        "width": 40,
        "height": 40,
        "depth": 248
      },
      "transform": {
        "position": [0, 265, 161.25],
        "rotation": [180, -90, 0]
      },
      "material_ref": "espuma_acustica",
      "properties": {
        "tipo": "Trampa Graves Esquinera Sur"
      }
    }
])

# 3. Paneles de primera reflexión laterales
# Left wall is X = -124. Panel thickness = 10. Center X = -119.
# Right wall is X = 124. Center X = 119.
# Z = -125 (midpoint between speakers and listener)
new_nodes.extend([
    {
      "id": "panel_reflexion_izq",
      "layer": "ACUSTICA",
      "clase": "TRATAMIENTO_ACUSTICO",
      "geometry": {
        "type": "BoxGeometry",
        "width": 10,
        "height": 120,
        "depth": 80
      },
      "transform": {
        "position": [-119, 110, -125],
        "rotation": [0, 0, 0]
      },
      "material_ref": "panel_acustico_negro",
      "properties": {
        "tipo": "Panel Reflexion Izquierdo"
      }
    },
    {
      "id": "panel_reflexion_der",
      "layer": "ACUSTICA",
      "clase": "TRATAMIENTO_ACUSTICO",
      "geometry": {
        "type": "BoxGeometry",
        "width": 10,
        "height": 120,
        "depth": 80
      },
      "transform": {
        "position": [119, 110, -125],
        "rotation": [0, 0, 0]
      },
      "material_ref": "panel_acustico_negro",
      "properties": {
        "tipo": "Panel Reflexion Derecho"
      }
    }
])

data['nodes'] = new_nodes

with open('proyecto_obra.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Actualizado.")
