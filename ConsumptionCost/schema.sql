/* (Beta) Export of data model ConsumptionCost of the subject dataModel.Consumption for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ConsumptionCost_type AS ENUM ('ConsumptionCost');
CREATE TABLE ConsumptionCost (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, energyConsumedAndCost JSON, month TEXT, name TEXT, owner JSON, source TEXT, type ConsumptionCost_type, year TEXT);