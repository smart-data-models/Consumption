<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。消费成本  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Consumption/blob/master/ConsumptionCost/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**各消费点消耗的能源及其成本的信息**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `consumptionPoint[*]`: 实体所指的消费点标识符。  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `energyConsumedAndCost[array]`: 阵列与能源消耗和成本，按能源类型划分。  - `id[*]`: 实体的唯一标识符  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `month[string]`: 该实体所指的月份。格式MM，例如：'07'  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: NGSI实体类型。它必须是ConsumptionCost。  - `year[string]`: 该实体所指的年份。格式为YYY，例如：'2022'。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `consumptionPoint`  - `energyConsumedAndCost`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
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
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        type: Geoproperty    
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
## ＃＃＃＃有效载荷的例子  
#### ConsumptionCost NGSI-v2 关键值示例  
这里是一个以JSON-LD格式作为key-values的ConsumptionCost的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### 消费成本NGSI-v2归一化示例  
下面是一个规范化的JSON-LD格式的ConsumptionCost的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### ConsumptionCost NGSI-LD关键值示例  
这里是一个以JSON-LD格式作为key-values的ConsumptionCost的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### 消费成本NGSI-LD归一化示例  
下面是一个规范化的JSON-LD格式的ConsumptionCost的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
