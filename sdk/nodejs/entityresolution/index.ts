// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { GetSchemaMappingArgs, GetSchemaMappingResult, GetSchemaMappingOutputArgs } from "./getSchemaMapping";
export const getSchemaMapping: typeof import("./getSchemaMapping").getSchemaMapping = null as any;
export const getSchemaMappingOutput: typeof import("./getSchemaMapping").getSchemaMappingOutput = null as any;
utilities.lazyLoad(exports, ["getSchemaMapping","getSchemaMappingOutput"], () => require("./getSchemaMapping"));

export { SchemaMappingArgs } from "./schemaMapping";
export type SchemaMapping = import("./schemaMapping").SchemaMapping;
export const SchemaMapping: typeof import("./schemaMapping").SchemaMapping = null as any;
utilities.lazyLoad(exports, ["SchemaMapping"], () => require("./schemaMapping"));


// Export enums:
export * from "../types/enums/entityresolution";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:entityresolution:SchemaMapping":
                return new SchemaMapping(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "entityresolution", _module)
