// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IoTAnalytics::Datastore
 */
export class Datastore extends pulumi.CustomResource {
    /**
     * Get an existing Datastore resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Datastore {
        return new Datastore(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iotanalytics:Datastore';

    /**
     * Returns true if the given object is an instance of Datastore.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Datastore {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Datastore.__pulumiType;
    }

    public readonly datastoreName!: pulumi.Output<string | undefined>;
    public readonly datastorePartitions!: pulumi.Output<outputs.iotanalytics.DatastorePartitions | undefined>;
    public readonly datastoreStorage!: pulumi.Output<outputs.iotanalytics.DatastoreStorage | undefined>;
    public readonly fileFormatConfiguration!: pulumi.Output<outputs.iotanalytics.DatastoreFileFormatConfiguration | undefined>;
    public readonly retentionPeriod!: pulumi.Output<outputs.iotanalytics.DatastoreRetentionPeriod | undefined>;
    public readonly tags!: pulumi.Output<outputs.iotanalytics.DatastoreTag[] | undefined>;

    /**
     * Create a Datastore resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DatastoreArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["datastoreName"] = args ? args.datastoreName : undefined;
            resourceInputs["datastorePartitions"] = args ? args.datastorePartitions : undefined;
            resourceInputs["datastoreStorage"] = args ? args.datastoreStorage : undefined;
            resourceInputs["fileFormatConfiguration"] = args ? args.fileFormatConfiguration : undefined;
            resourceInputs["retentionPeriod"] = args ? args.retentionPeriod : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["datastoreName"] = undefined /*out*/;
            resourceInputs["datastorePartitions"] = undefined /*out*/;
            resourceInputs["datastoreStorage"] = undefined /*out*/;
            resourceInputs["fileFormatConfiguration"] = undefined /*out*/;
            resourceInputs["retentionPeriod"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Datastore.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Datastore resource.
 */
export interface DatastoreArgs {
    datastoreName?: pulumi.Input<string>;
    datastorePartitions?: pulumi.Input<inputs.iotanalytics.DatastorePartitionsArgs>;
    datastoreStorage?: pulumi.Input<inputs.iotanalytics.DatastoreStorageArgs>;
    fileFormatConfiguration?: pulumi.Input<inputs.iotanalytics.DatastoreFileFormatConfigurationArgs>;
    retentionPeriod?: pulumi.Input<inputs.iotanalytics.DatastoreRetentionPeriodArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.iotanalytics.DatastoreTagArgs>[]>;
}
