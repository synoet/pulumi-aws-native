// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AppSync::Resolver
 *
 * @deprecated Resolver is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Resolver extends pulumi.CustomResource {
    /**
     * Get an existing Resolver resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Resolver {
        pulumi.log.warn("Resolver is deprecated: Resolver is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Resolver(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:appsync:Resolver';

    /**
     * Returns true if the given object is an instance of Resolver.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Resolver {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Resolver.__pulumiType;
    }

    public readonly apiId!: pulumi.Output<string>;
    public readonly cachingConfig!: pulumi.Output<outputs.appsync.ResolverCachingConfig | undefined>;
    public readonly code!: pulumi.Output<string | undefined>;
    public readonly codeS3Location!: pulumi.Output<string | undefined>;
    public readonly dataSourceName!: pulumi.Output<string | undefined>;
    public readonly fieldName!: pulumi.Output<string>;
    public readonly kind!: pulumi.Output<string | undefined>;
    public readonly maxBatchSize!: pulumi.Output<number | undefined>;
    public readonly pipelineConfig!: pulumi.Output<outputs.appsync.ResolverPipelineConfig | undefined>;
    public readonly requestMappingTemplate!: pulumi.Output<string | undefined>;
    public readonly requestMappingTemplateS3Location!: pulumi.Output<string | undefined>;
    public /*out*/ readonly resolverArn!: pulumi.Output<string>;
    public readonly responseMappingTemplate!: pulumi.Output<string | undefined>;
    public readonly responseMappingTemplateS3Location!: pulumi.Output<string | undefined>;
    public readonly runtime!: pulumi.Output<outputs.appsync.ResolverAppSyncRuntime | undefined>;
    public readonly syncConfig!: pulumi.Output<outputs.appsync.ResolverSyncConfig | undefined>;
    public readonly typeName!: pulumi.Output<string>;

    /**
     * Create a Resolver resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Resolver is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ResolverArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Resolver is deprecated: Resolver is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.apiId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'apiId'");
            }
            if ((!args || args.fieldName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'fieldName'");
            }
            if ((!args || args.typeName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'typeName'");
            }
            resourceInputs["apiId"] = args ? args.apiId : undefined;
            resourceInputs["cachingConfig"] = args ? args.cachingConfig : undefined;
            resourceInputs["code"] = args ? args.code : undefined;
            resourceInputs["codeS3Location"] = args ? args.codeS3Location : undefined;
            resourceInputs["dataSourceName"] = args ? args.dataSourceName : undefined;
            resourceInputs["fieldName"] = args ? args.fieldName : undefined;
            resourceInputs["kind"] = args ? args.kind : undefined;
            resourceInputs["maxBatchSize"] = args ? args.maxBatchSize : undefined;
            resourceInputs["pipelineConfig"] = args ? args.pipelineConfig : undefined;
            resourceInputs["requestMappingTemplate"] = args ? args.requestMappingTemplate : undefined;
            resourceInputs["requestMappingTemplateS3Location"] = args ? args.requestMappingTemplateS3Location : undefined;
            resourceInputs["responseMappingTemplate"] = args ? args.responseMappingTemplate : undefined;
            resourceInputs["responseMappingTemplateS3Location"] = args ? args.responseMappingTemplateS3Location : undefined;
            resourceInputs["runtime"] = args ? args.runtime : undefined;
            resourceInputs["syncConfig"] = args ? args.syncConfig : undefined;
            resourceInputs["typeName"] = args ? args.typeName : undefined;
            resourceInputs["resolverArn"] = undefined /*out*/;
        } else {
            resourceInputs["apiId"] = undefined /*out*/;
            resourceInputs["cachingConfig"] = undefined /*out*/;
            resourceInputs["code"] = undefined /*out*/;
            resourceInputs["codeS3Location"] = undefined /*out*/;
            resourceInputs["dataSourceName"] = undefined /*out*/;
            resourceInputs["fieldName"] = undefined /*out*/;
            resourceInputs["kind"] = undefined /*out*/;
            resourceInputs["maxBatchSize"] = undefined /*out*/;
            resourceInputs["pipelineConfig"] = undefined /*out*/;
            resourceInputs["requestMappingTemplate"] = undefined /*out*/;
            resourceInputs["requestMappingTemplateS3Location"] = undefined /*out*/;
            resourceInputs["resolverArn"] = undefined /*out*/;
            resourceInputs["responseMappingTemplate"] = undefined /*out*/;
            resourceInputs["responseMappingTemplateS3Location"] = undefined /*out*/;
            resourceInputs["runtime"] = undefined /*out*/;
            resourceInputs["syncConfig"] = undefined /*out*/;
            resourceInputs["typeName"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Resolver.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Resolver resource.
 */
export interface ResolverArgs {
    apiId: pulumi.Input<string>;
    cachingConfig?: pulumi.Input<inputs.appsync.ResolverCachingConfigArgs>;
    code?: pulumi.Input<string>;
    codeS3Location?: pulumi.Input<string>;
    dataSourceName?: pulumi.Input<string>;
    fieldName: pulumi.Input<string>;
    kind?: pulumi.Input<string>;
    maxBatchSize?: pulumi.Input<number>;
    pipelineConfig?: pulumi.Input<inputs.appsync.ResolverPipelineConfigArgs>;
    requestMappingTemplate?: pulumi.Input<string>;
    requestMappingTemplateS3Location?: pulumi.Input<string>;
    responseMappingTemplate?: pulumi.Input<string>;
    responseMappingTemplateS3Location?: pulumi.Input<string>;
    runtime?: pulumi.Input<inputs.appsync.ResolverAppSyncRuntimeArgs>;
    syncConfig?: pulumi.Input<inputs.appsync.ResolverSyncConfigArgs>;
    typeName: pulumi.Input<string>;
}
