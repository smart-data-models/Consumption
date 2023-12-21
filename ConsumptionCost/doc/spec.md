<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: ConsumptionCost    
=======================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.Consumption/blob/master/ConsumptionCost/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **Information of energy consumed and its cost by consumption point**    
version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government      
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `consumptionPoint[*]`: Consumption point identifier which to entity refers  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `energyConsumedAndCost[array]`: Array with energy consumption and cost by type of energy  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `month[string]`: The month to which the entity refers. Format MM, ex:'07'  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `type[string]`: NGSI entity type. It has to be ConsumptionCost  - `year[string]`: The year to which the entity refers. Format YYYY, ex:'2022'  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Required properties    
- `consumptionPoint`  - `energyConsumedAndCost`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Data Model description of properties    
Sorted alphabetically (click for details)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
ConsumptionCost:      
  description: Information of energy consumed and its cost by consumption point      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    consumptionPoint:      
      description: Consumption point identifier which to entity refers      
      oneOf:      
        - format: uuid      
          type: string      
        - anyOf:      
            - description: Identifier format of any NGSI entity      
              maxLength: 256      
              minLength: 1      
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
              type: string      
              x-ngsi:      
                type: Property      
            - description: Identifier format of any NGSI entity      
              format: uri      
              type: string      
              x-ngsi:      
                type: Property      
          description: Unique identifier of the entity      
          x-ngsi:      
            type: Property      
      x-ngsi:      
        type: Relationship      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    energyConsumedAndCost:      
      description: Array with energy consumption and cost by type of energy      
      items:      
        description: Entity with the energy consumed and its cost by type of energy      
        properties:      
          energyConsumed:      
            description: Amount of energy consumed      
            properties:      
              measurementUnit:      
                description: 'Measurement unit used. Official list at https://unece.org/trade/documents/2021/06/uncefact-rec20'      
                oneOf:      
                  - enum:      
                      - MTQ      
                    type: string      
                  - enum:      
                      - KWH      
                    type: string      
                x-ngsi:      
                  type: Property      
                  units: "[MTQ, KWH]"      
              value:      
                description: Value of the amount of the energy consumed      
                type: number      
                x-ngsi:      
                  type: Property      
            type: object      
            x-ngsi:      
              type: Property      
          energyType:      
            description: Type of energy      
            type: string      
            x-ngsi:      
              type: Property      
          id:      
            description: 'Identifier of consumption lecture entity. For example, CUPS in Spain'      
            items:      
              oneOf:      
                - format: uri      
                  type: string      
                - anyOf:      
                    - description: Identifier format of any NGSI entity      
                      maxLength: 256      
                      minLength: 1      
                      pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
                      type: string      
                      x-ngsi:      
                        type: Property      
                    - description: Identifier format of any NGSI entity      
                      format: uri      
                      type: string      
                      x-ngsi:      
                        type: Property      
                  description: Unique identifier of the entity      
                  x-ngsi:      
                    type: Property      
            type: string      
            x-ngsi:      
              type: Property      
          supplyName:      
            description: Name of the supply company      
            type: string      
            x-ngsi:      
              type: Property      
          totalCost:      
            description: Amount of cost by energy consumed      
            properties:      
              currency:      
                description: 'Currency names in ISO-4217 format. Enum:''[EUR, USD, GPD, JPY]''. Official list https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/lists/list_one.xls'      
                enum:      
                  - EUR      
                  - GPD      
                  - JPY      
                  - USD      
                type: string      
                x-ngsi:      
                  type: Property      
              value:      
                description: Value of the amount of the cost for energy consumed      
                type: number      
                x-ngsi:      
                  type: Property      
            type: object      
            x-ngsi:      
              type: Property      
        type: object      
        x-ngsi:      
          type: Property      
      minItems: 1      
      type: array      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    month:      
      description: 'The month to which the entity refers. Format MM, ex:''07'''      
      pattern: (0[1-9]|1[0-2])      
      type: string      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI entity type. It has to be ConsumptionCost      
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
## Example payloads      
#### ConsumptionCost NGSI-v2 key-values Example      
Here is an example of a ConsumptionCost in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
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
      "id": "did:ener:ele:ESXXXXXXXXXXXXXXXXXXXX",  
      "energyType": "electricity",  
      "supplyName": "Electric Company, S.A.",  
      "energyConsumed": {  
        "measurementUnit": "KWH",  
        "value": 800.0  
      },  
      "totalCost": {  
        "currency": "EUR",  
        "value": 374.0  
      }  
    },  
    {  
      "id": "did:ener:gas:ESXXXXXXXXXXXXXXXXXXXX",  
      "energyType": "gas",  
      "supplyName": "Gas Company, S.A.",  
      "energyConsumed": {  
        "measurementUnit": "MTQ",  
        "value": 35.0  
      },  
      "totalCost": {  
        "currency": "EUR",  
        "value": 250.32  
      }  
    },  
    {  
      "id": "did:ener:wat:02060767",  
      "energyType": "water",  
      "supplyName": "Water Company",  
      "energyConsumed": {  
        "measurementUnit": "MTQ",  
        "value": 33.0  
      },  
      "totalCost": {  
        "currency": "EUR",  
        "value": 110.34  
      }  
    }  
  ]  
}  
```  
</details>    
#### ConsumptionCost NGSI-v2 normalized Example      
Here is an example of a ConsumptionCost in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
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
    "type": "Text",  
    "value": "did:consumpoint:EN04"  
  },  
  "energyConsumedAndCost": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "id": "did:ener:ele:ESXXXXXXXXXXXXXXXXXXXX",  
        "energyType": "electricity",  
        "supplyName": "Electric Company, S.A.",  
        "energyConsumed": {  
          "measurementUnit": "KWH",  
          "value": 800.0  
        },  
        "totalCost": {  
          "currency": "EUR",  
          "value": 374.0  
        }  
      }  
    ]  
  }  
}  
```  
</details>    
#### ConsumptionCost NGSI-LD key-values Example      
Here is an example of a ConsumptionCost in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
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
      "id": "did:ener:ele:ESXXXXXXXXXXXXXXXXXXXX",  
      "energyType": "electricity",  
      "supplyName": "Electric Company, S.A.",  
      "energyConsumed": {  
        "measurementUnit": "KWH",  
        "value": 800.0  
      },  
      "totalCost": {  
        "currency": "EUR",  
        "value": 374.0  
      }  
    },  
    {  
      "id": "did:ener:gas:ESXXXXXXXXXXXXXXXXXXXX",  
      "energyType": "gas",  
      "supplyName": "Gas Company, S.A.",  
      "energyConsumed": {  
        "measurementUnit": "MTQ",  
        "value": 35.0  
      },  
      "totalCost": {  
        "currency": "EUR",  
        "value": 250.32  
      }  
    },  
    {  
      "id": "did:ener:wat:02060767",  
      "energyType": "water",  
      "supplyName": "Water Company",  
      "energyConsumed": {  
        "measurementUnit": "MTQ",  
        "value": 33.0  
      },  
      "totalCost": {  
        "currency": "EUR",  
        "value": 110.34  
      }  
    }  
  ],  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Consumption/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### ConsumptionCost NGSI-LD normalized Example      
Here is an example of a ConsumptionCost in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
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
    "value": "did:consumpoint:EN04"  
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
        "totalCost": {  
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
  ],  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Consumption/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
