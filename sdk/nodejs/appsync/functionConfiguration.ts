// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AppSync::FunctionConfiguration
 *
 * @deprecated FunctionConfiguration is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class FunctionConfiguration extends pulumi.CustomResource {
    /**
     * Get an existing FunctionConfiguration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): FunctionConfiguration {
        pulumi.log.warn("FunctionConfiguration is deprecated: FunctionConfiguration is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new FunctionConfiguration(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:appsync:FunctionConfiguration';

    /**
     * Returns true if the given object is an instance of FunctionConfiguration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FunctionConfiguration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FunctionConfiguration.__pulumiType;
    }

    public readonly apiId!: pulumi.Output<string>;
    public readonly code!: pulumi.Output<string | undefined>;
    public readonly codeS3Location!: pulumi.Output<string | undefined>;
    public readonly dataSourceName!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public /*out*/ readonly functionArn!: pulumi.Output<string>;
    public /*out*/ readonly functionId!: pulumi.Output<string>;
    public readonly functionVersion!: pulumi.Output<string | undefined>;
    public readonly maxBatchSize!: pulumi.Output<number | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly requestMappingTemplate!: pulumi.Output<string | undefined>;
    public readonly requestMappingTemplateS3Location!: pulumi.Output<string | undefined>;
    public readonly responseMappingTemplate!: pulumi.Output<string | undefined>;
    public readonly responseMappingTemplateS3Location!: pulumi.Output<string | undefined>;
    public readonly runtime!: pulumi.Output<outputs.appsync.FunctionConfigurationAppSyncRuntime | undefined>;
    public readonly syncConfig!: pulumi.Output<outputs.appsync.FunctionConfigurationSyncConfig | undefined>;

    /**
     * Create a FunctionConfiguration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated FunctionConfiguration is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: FunctionConfigurationArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("FunctionConfiguration is deprecated: FunctionConfiguration is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.apiId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'apiId'");
            }
            if ((!args || args.dataSourceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dataSourceName'");
            }
            resourceInputs["apiId"] = args ? args.apiId : undefined;
            resourceInputs["code"] = args ? args.code : undefined;
            resourceInputs["codeS3Location"] = args ? args.codeS3Location : undefined;
            resourceInputs["dataSourceName"] = args ? args.dataSourceName : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["functionVersion"] = args ? args.functionVersion : undefined;
            resourceInputs["maxBatchSize"] = args ? args.maxBatchSize : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["requestMappingTemplate"] = args ? args.requestMappingTemplate : undefined;
            resourceInputs["requestMappingTemplateS3Location"] = args ? args.requestMappingTemplateS3Location : undefined;
            resourceInputs["responseMappingTemplate"] = args ? args.responseMappingTemplate : undefined;
            resourceInputs["responseMappingTemplateS3Location"] = args ? args.responseMappingTemplateS3Location : undefined;
            resourceInputs["runtime"] = args ? args.runtime : undefined;
            resourceInputs["syncConfig"] = args ? args.syncConfig : undefined;
            resourceInputs["functionArn"] = undefined /*out*/;
            resourceInputs["functionId"] = undefined /*out*/;
        } else {
            resourceInputs["apiId"] = undefined /*out*/;
            resourceInputs["code"] = undefined /*out*/;
            resourceInputs["codeS3Location"] = undefined /*out*/;
            resourceInputs["dataSourceName"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["functionArn"] = undefined /*out*/;
            resourceInputs["functionId"] = undefined /*out*/;
            resourceInputs["functionVersion"] = undefined /*out*/;
            resourceInputs["maxBatchSize"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["requestMappingTemplate"] = undefined /*out*/;
            resourceInputs["requestMappingTemplateS3Location"] = undefined /*out*/;
            resourceInputs["responseMappingTemplate"] = undefined /*out*/;
            resourceInputs["responseMappingTemplateS3Location"] = undefined /*out*/;
            resourceInputs["runtime"] = undefined /*out*/;
            resourceInputs["syncConfig"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(FunctionConfiguration.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a FunctionConfiguration resource.
 */
export interface FunctionConfigurationArgs {
    apiId: pulumi.Input<string>;
    code?: pulumi.Input<string>;
    codeS3Location?: pulumi.Input<string>;
    dataSourceName: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    functionVersion?: pulumi.Input<string>;
    maxBatchSize?: pulumi.Input<number>;
    name?: pulumi.Input<string>;
    requestMappingTemplate?: pulumi.Input<string>;
    requestMappingTemplateS3Location?: pulumi.Input<string>;
    responseMappingTemplate?: pulumi.Input<string>;
    responseMappingTemplateS3Location?: pulumi.Input<string>;
    runtime?: pulumi.Input<inputs.appsync.FunctionConfigurationAppSyncRuntimeArgs>;
    syncConfig?: pulumi.Input<inputs.appsync.FunctionConfigurationSyncConfigArgs>;
}
