// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * SchemaMapping defined in AWS Entity Resolution service
 */
export function getSchemaMapping(args: GetSchemaMappingArgs, opts?: pulumi.InvokeOptions): Promise<GetSchemaMappingResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:entityresolution:getSchemaMapping", {
        "schemaName": args.schemaName,
    }, opts);
}

export interface GetSchemaMappingArgs {
    /**
     * The name of the SchemaMapping
     */
    schemaName: string;
}

export interface GetSchemaMappingResult {
    readonly createdAt?: string;
    readonly schemaArn?: string;
    readonly tags?: outputs.entityresolution.SchemaMappingTag[];
    readonly updatedAt?: string;
}
/**
 * SchemaMapping defined in AWS Entity Resolution service
 */
export function getSchemaMappingOutput(args: GetSchemaMappingOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSchemaMappingResult> {
    return pulumi.output(args).apply((a: any) => getSchemaMapping(a, opts))
}

export interface GetSchemaMappingOutputArgs {
    /**
     * The name of the SchemaMapping
     */
    schemaName: pulumi.Input<string>;
}
