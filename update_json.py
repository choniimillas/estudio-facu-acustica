import json

with open('proyecto_obra.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_nodes = []
for node in data['nodes']:
    # Remove old things
    if node['id'] in ['organo_teclados', 'silla_oficina', 'panel_techo', 'panel_reflexion_techo', 
                      'trampa_graves_nw', 'trampa_graves_ne', 'trampa_graves_sw', 'trampa_graves_se']:
        continue
    new_nodes.append(node)

# Add updated organ keys
new_nodes.extend([
    {
      "id": "organo_teclas_blancas",
      "layer": "MOBILIARIO",
      "geometry": {
        "type": "BoxGeometry",
        "width": 20,
        "height": 5,
        "depth": 100
      },
      "transform": {
        "position": [-80, 75, 0.5],
        "rotation": [0, 0, 0]
      },
      "material_ref": "plastico_teclado",
      "properties": {
        "tipo": "Teclas Blancas Organo"
      }
    },
    {
      "id": "organo_teclas_negras",
      "layer": "MOBILIARIO",
      "geometry": {
        "type": "BoxGeometry",
        "width": 10,
        "height": 7,
        "depth": 95
      },
      "transform": {
        "position": [-83, 76, 0.5],
        "rotation": [0, 0, 0]
      },
      "material_ref": "negro_parlante",
      "properties": {
        "tipo": "Teclas Negras Organo"
      }
    }
])

# Add proper chair
new_nodes.extend([
    {
      "id": "silla_asiento",
      "layer": "MOBILIARIO",
      "geometry": {
        "type": "BoxGeometry",
        "width": 50,
        "height": 8,
        "depth": 50
      },
      "transform": {
        "position": [0, 45, -100],
        "rotation": [0, 0, 0]
      },
      "material_ref": "tela_sillon",
      "properties": {
        "tipo": "Asiento Silla"
      }
    },
    {
      "id": "silla_respaldo",
      "layer": "MOBILIARIO",
      "geometry": {
        "type": "BoxGeometry",
        "width": 45,
        "height": 45,
        "depth": 8
      },
      "transform": {
        "position": [0, 72, -75],
        "rotation": [-10, 0, 0]
      },
      "material_ref": "tela_sillon",
      "properties": {
        "tipo": "Respaldo Silla"
      }
    },
    {
      "id": "silla_pilar",
      "layer": "MOBILIARIO",
      "geometry": {
        "type": "BoxGeometry",
        "width": 5,
        "height": 35,
        "depth": 5
      },
      "transform": {
        "position": [0, 25, -100],
        "rotation": [0, 0, 0]
      },
      "material_ref": "hierro_patas",
      "properties": {
        "tipo": "Pilar Silla"
      }
    },
    {
      "id": "silla_base",
      "layer": "MOBILIARIO",
      "geometry": {
        "type": "BoxGeometry",
        "width": 40,
        "height": 5,
        "depth": 40
      },
      "transform": {
        "position": [0, 5, -100],
        "rotation": [0, 45, 0]
      },
      "material_ref": "hierro_patas",
      "properties": {
        "tipo": "Base Silla"
      }
    }
])

# Add relocated ceiling panel
new_nodes.append({
    "id": "panel_techo",
    "layer": "ACUSTICA",
    "clase": "TRATAMIENTO_ACUSTICO",
    "geometry": {
        "type": "BoxGeometry",
        "width": 180,
        "height": 10,
        "depth": 150
    },
    "transform": {
        "position": [0, 275, -125],
        "rotation": [0, 90, 0]
    },
    "material_ref": "panel_acustico_negro",
    "properties": {
        "tipo": "Panel Nube Techo"
    }
})

# Add relocated bass traps (soffit traps at ceiling corners)
new_nodes.extend([
    {
      "id": "trampa_graves_norte_techo",
      "layer": "ACUSTICA",
      "clase": "TRATAMIENTO_ACUSTICO",
      "geometry": {
        "type": "BoxGeometry",
        "width": 260,
        "height": 30,
        "depth": 30
      },
      "transform": {
        "position": [0, 285, -173],
        "rotation": [0, 0, 0]
      },
      "material_ref": "espuma_acustica",
      "properties": {
        "tipo": "Trampa Graves Techo Norte"
      }
    },
    {
      "id": "trampa_graves_sur_techo",
      "layer": "ACUSTICA",
      "clase": "TRATAMIENTO_ACUSTICO",
      "geometry": {
        "type": "BoxGeometry",
        "width": 260,
        "height": 30,
        "depth": 30
      },
      "transform": {
        "position": [0, 285, 173],
        "rotation": [0, 0, 0]
      },
      "material_ref": "espuma_acustica",
      "properties": {
        "tipo": "Trampa Graves Techo Sur"
      }
    }
])

data['nodes'] = new_nodes

with open('proyecto_obra.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Modificaciones aplicadas con éxito.")
