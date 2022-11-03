<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Coût de la consommation  
================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Consumption/blob/master/ConsumptionCost/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Information sur l'énergie consommée et son coût par point de consommation**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `consumptionPoint[*]`: Identifiant du point de consommation auquel l'entité se réfère.  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `energyConsumedAndCost[array]`: Tableau avec la consommation d'énergie et le coût par type d'énergie.  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `month[string]`: Le mois auquel l'entité se réfère. Format MM, ex : "07  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type[string]`: Type d'entité NGSI. Il doit s'agir de ConsumptionCost.  - `year[string]`: L'année à laquelle l'entité se réfère. Format YYYY, ex : "2022  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `consumptionPoint`  - `energyConsumedAndCost`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ConsumptionCost:    
  description: 'Information of energy consumed and its cost by consumption point'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    consumptionPoint:    
      description: 'Consumption point identifier which to entity refers.'    
      oneOf:    
        - format: uuid    
          type: string    
        - anyOf: &anyof    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
          description: 'Property. Unique identifier of the entity'    
      x-ngsi:    
        type: Relationship    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    energyConsumedAndCost:    
      description: 'Array with energy consumption and cost by type of energy.'    
      items:    
        - description: 'Property. Entity with the energy consumed and its cost by type of energy.'    
          properties:    
            energyConsumed:    
              description: 'Property. Amount of energy consumed.'    
              properties:    
                measurementUnit:    
                  description: 'Property. Measurement unit used. Units:''[MTQ, KWH]''. Official list at https://unece.org/trade/documents/2021/06/uncefact-rec20'    
                  oneOf:    
                    - enum:    
                        - MTQ    
                      type: string    
                    - enum:    
                        - KWH    
                      type: string    
                value:    
                  description: 'Property. Value of the amount of the energy consumed.'    
                  type: number    
              type: object    
            energyType:    
              description: 'Property. Type of energy.'    
              type: string    
            id:    
              description: 'Property. Identifier of consumption lecture entity. For example, CUPS in Spain.'    
              items:    
                oneOf:    
                  - format: uri    
                    type: string    
                  - anyOf: *anyof    
                    description: 'Property. Unique identifier of the entity'    
              type: string    
            supplyName:    
              description: 'Property. Name of the supply company.'    
              type: string    
            totalCost:    
              description: 'Property. Amount of cost by energy consumed.'    
              properties:    
                currency:    
                  description: 'Property. Currency names in ISO-4217 format. Enum:''[EUR, USD, GPD, JPY]''. Official list https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/lists/list_one.xls'    
                  enum:    
                    - EUR    
                    - GPD    
                    - JPY    
                    - USD    
                  type: string    
                value:    
                  description: 'Property. Value of the amount of the cost for energy consumed.'    
                  type: number    
              type: object    
          type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: *anyof    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    month:    
      description: 'The month to which the entity refers. Format MM, ex:''07'''    
      pattern: (0[1-9]|1[0-2])    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be ConsumptionCost.'    
      enum:    
        - ConsumptionCost    
      type: string    
      x-ngsi:    
        type: Property    
    year:    
      description: 'The year to which the entity refers. Format YYYY, ex:''2022'''    
      pattern: (2[0-9]{3})    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - consumptionPoint    
    - energyConsumedAndCost    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Consumption/blob/master/ConsumptionCost/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Consumption/ConsumptionCost/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### ConsommationCoût Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de ConsumptionCost au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "did:enerconsumcost:2022-07-3325",  
    "type": "ConsumptionCost",  
    "year": "2022",  
    "month": "07",  
    "consumptionPoint":  
        "did:consumpoint:EN04"  
    ,  
    "energyConsumedAndCost": [{  
            "id": "did:ener:ele:ESXXXXXXXXXXXXXXXXXXXX",  
            "energyType": "electricity",  
            "supplyName": "Electric Company, S.A.",  
            "energyConsumed": {  
                "measurementUnit": "KWH",  
                "value": 800.00  
            },  
            "energyAmount": {  
                "currency": "EUR",  
                "value": 374.00  
            }  
        },  
        {  
            "id": "did:ener:gas:ESXXXXXXXXXXXXXXXXXXXX",  
            "type": "gas",  
            "supplyName": "Gas Company, S.A.",  
            "consumption": {  
                "measurementUnit": "MTQ",  
                "value": 35.00  
            },  
            "amount": {  
                "currency": "EUR",  
                "value": 250.32  
            }  
        },  
        {  
            "id": "did:ener:wat:02060767",  
            "type": "water",  
            "supplyName": "Water Company",  
            "consumption": {  
                "measurementUnit": "MTQ",  
                "value": 33.00  
            },  
            "amount": {  
                "currency": "EUR",  
                "value": 110.34  
            }  
        }  
    ]  
}  
```  
</details>  
#### Coût de consommation NGSI-v2 normalisé Exemple  
Voici un exemple d'un ConsumptionCost au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "did:enerconsumcost:2022-07-3325",  
  "type": "ConsumptionCost",  
  "year": {  
    "type": "Text",  
    "value": "2022"  
  },  
  "month": {  
    "type": "Text",  
    "value": "07"  
  },  
  "consumptionPoint": {  
    "type": "Relationship",  
    "value":  
      "did:consumpoint:EN04"  
  },  
  "energyConsumedAndCost": [  
    {  
      "type": "StructuredValue",  
      "value": {  
        "id": {  
          "type": "Text",  
          "value": "did:ener:ele:ESXXXXXXXXXXXXXXXXXXXX"  
        },  
        "energyType": {  
          "type": "Text",  
          "value": "electricity"  
        },  
        "supplyName": {  
          "type": "Text",  
          "value": "Electric Company, S.A."  
        },  
        "energyConsumed": {  
          "type": "StructuredValue",  
          "value": {  
            "measurementUnit": {  
              "type": "Text",  
              "value": "KWH"  
            },  
            "value": {  
              "type": "Number",  
              "value": 800.00  
            }  
          }  
        },  
        "energyAmount": {  
          "type": "StructuredValue",  
          "value": {  
            "currency": {  
              "type": "Text",  
              "value": "EUR"  
            },  
            "value": {  
              "type": "Number",  
              "value": 374.00  
            }  
          }  
        }  
      }  
    }  
  ]  
}  
```  
</details>  
#### ConsommationCoût Valeurs-clés NGSI-LD Exemple  
Voici un exemple de ConsumptionCost au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "did:enerconsumcost:2022-07-3325",  
    "type": "ConsumptionCost",  
    "year": "2022",  
    "month": "07",  
    "consumptionPoint": "did:consumpoint:EN04",  
    "energyConsumedAndCost": [  
        {  
            "id": {  
                "type": "Property",  
                "value": "did:ener:ele:ESXXXXXXXXXXXXXXXXXXXX"  
            },  
            "energyType": {  
                "type": "Property",  
                "value": "electricity"  
            },  
            "supplyName": {  
                "type": "Property",  
                "value": "Electric Company, S.A."  
            },  
            "energyConsumed": {  
                "measurementUnit": "KWH",  
                "value": 800.0  
            },  
            "energyAmount": {  
                "currency": "EUR",  
                "value": 374.0  
            }  
        }  
    ],  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Consumption/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Consumption/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Coût de consommation NGSI-LD normalisé Exemple  
Voici un exemple d'un ConsumptionCost au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "did:enerconsumcost:2022-07-3325",  
    "type": "ConsumptionCost",  
    "year": {  
        "type": "Property",  
        "value": "2022"  
    },  
    "month": {  
        "type": "Property",  
        "value": "07"  
    },  
    "consumptionPoint": {  
        "type": "Relationship",  
        "object": "did:consumpoint:EN04"  
    },  
    "energyConsumedAndCost": [  
        {  
            "type": "Property",  
            "value": {  
                "id": {  
                    "type": "Property",  
                    "value": "did:ener:ele:ESXXXXXXXXXXXXXXXXXXXX"  
                },  
                "energyType": {  
                    "type": "Property",  
                    "value": "electricity"  
                },  
                "supplyName": {  
                    "type": "Property",  
                    "value": "Electric Company, S.A."  
                },  
                "energyConsumed": {  
                    "type": "Property",  
                    "value": {  
                        "measurementUnit": {  
                            "type": "Property",  
                            "value": "KWH"  
                        },  
                        "value": {  
                            "type": "Property",  
                            "value": 800.0  
                        }  
                    }  
                },  
                "energyAmount": {  
                    "type": "Property",  
                    "value": {  
                        "currency": {  
                            "type": "Text",  
                            "value": "EUR"  
                        },  
                        "value": {  
                            "type": "Number",  
                            "value": 374.0  
                        }  
                    }  
                }  
            }  
        }  
    ],  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Consumption/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Consumption/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
