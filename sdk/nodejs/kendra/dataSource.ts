// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Kendra DataSource
 */
export class DataSource extends pulumi.CustomResource {
    /**
     * Get an existing DataSource resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DataSource {
        return new DataSource(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:kendra:DataSource';

    /**
     * Returns true if the given object is an instance of DataSource.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DataSource {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DataSource.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly dataSourceConfiguration!: pulumi.Output<outputs.kendra.DataSourceConfiguration | undefined>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly indexId!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public readonly roleArn!: pulumi.Output<string | undefined>;
    public readonly schedule!: pulumi.Output<string | undefined>;
    /**
     * Tags for labeling the data source
     */
    public readonly tags!: pulumi.Output<outputs.kendra.DataSourceTag[] | undefined>;
    public readonly type!: pulumi.Output<enums.kendra.DataSourceType>;

    /**
     * Create a DataSource resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DataSourceArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.indexId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'indexId'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            inputs["dataSourceConfiguration"] = args ? args.dataSourceConfiguration : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["indexId"] = args ? args.indexId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["roleArn"] = args ? args.roleArn : undefined;
            inputs["schedule"] = args ? args.schedule : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["arn"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["dataSourceConfiguration"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["indexId"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["roleArn"] = undefined /*out*/;
            inputs["schedule"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["type"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(DataSource.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a DataSource resource.
 */
export interface DataSourceArgs {
    dataSourceConfiguration?: pulumi.Input<inputs.kendra.DataSourceConfigurationArgs>;
    description?: pulumi.Input<string>;
    indexId: pulumi.Input<string>;
    name: pulumi.Input<string>;
    roleArn?: pulumi.Input<string>;
    schedule?: pulumi.Input<string>;
    /**
     * Tags for labeling the data source
     */
    tags?: pulumi.Input<pulumi.Input<inputs.kendra.DataSourceTagArgs>[]>;
    type: pulumi.Input<enums.kendra.DataSourceType>;
}
