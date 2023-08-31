// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AppIntegrations::DataIntegration
 */
export class DataIntegration extends pulumi.CustomResource {
    /**
     * Get an existing DataIntegration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DataIntegration {
        return new DataIntegration(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:appintegrations:DataIntegration';

    /**
     * Returns true if the given object is an instance of DataIntegration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DataIntegration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DataIntegration.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the data integration.
     */
    public /*out*/ readonly dataIntegrationArn!: pulumi.Output<string>;
    /**
     * The data integration description.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The configuration for what files should be pulled from the source.
     */
    public readonly fileConfiguration!: pulumi.Output<outputs.appintegrations.DataIntegrationFileConfiguration | undefined>;
    /**
     * The KMS key of the data integration.
     */
    public readonly kmsKey!: pulumi.Output<string>;
    /**
     * The name of the data integration.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The configuration for what data should be pulled from the source.
     */
    public readonly objectConfiguration!: pulumi.Output<outputs.appintegrations.DataIntegrationObjectConfiguration | undefined>;
    /**
     * The name of the data and how often it should be pulled from the source.
     */
    public readonly scheduleConfig!: pulumi.Output<outputs.appintegrations.DataIntegrationScheduleConfig>;
    /**
     * The URI of the data source.
     */
    public readonly sourceUri!: pulumi.Output<string>;
    /**
     * The tags (keys and values) associated with the data integration.
     */
    public readonly tags!: pulumi.Output<outputs.appintegrations.DataIntegrationTag[] | undefined>;

    /**
     * Create a DataIntegration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DataIntegrationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.kmsKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'kmsKey'");
            }
            if ((!args || args.scheduleConfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'scheduleConfig'");
            }
            if ((!args || args.sourceUri === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sourceUri'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["fileConfiguration"] = args ? args.fileConfiguration : undefined;
            resourceInputs["kmsKey"] = args ? args.kmsKey : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["objectConfiguration"] = args ? args.objectConfiguration : undefined;
            resourceInputs["scheduleConfig"] = args ? args.scheduleConfig : undefined;
            resourceInputs["sourceUri"] = args ? args.sourceUri : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["dataIntegrationArn"] = undefined /*out*/;
        } else {
            resourceInputs["dataIntegrationArn"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["fileConfiguration"] = undefined /*out*/;
            resourceInputs["kmsKey"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["objectConfiguration"] = undefined /*out*/;
            resourceInputs["scheduleConfig"] = undefined /*out*/;
            resourceInputs["sourceUri"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["kmsKey", "scheduleConfig", "sourceUri"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(DataIntegration.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DataIntegration resource.
 */
export interface DataIntegrationArgs {
    /**
     * The data integration description.
     */
    description?: pulumi.Input<string>;
    /**
     * The configuration for what files should be pulled from the source.
     */
    fileConfiguration?: pulumi.Input<inputs.appintegrations.DataIntegrationFileConfigurationArgs>;
    /**
     * The KMS key of the data integration.
     */
    kmsKey: pulumi.Input<string>;
    /**
     * The name of the data integration.
     */
    name?: pulumi.Input<string>;
    /**
     * The configuration for what data should be pulled from the source.
     */
    objectConfiguration?: pulumi.Input<inputs.appintegrations.DataIntegrationObjectConfigurationArgs>;
    /**
     * The name of the data and how often it should be pulled from the source.
     */
    scheduleConfig: pulumi.Input<inputs.appintegrations.DataIntegrationScheduleConfigArgs>;
    /**
     * The URI of the data source.
     */
    sourceUri: pulumi.Input<string>;
    /**
     * The tags (keys and values) associated with the data integration.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.appintegrations.DataIntegrationTagArgs>[]>;
}
