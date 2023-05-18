// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * A storage lake of event data against which you can run complex SQL-based queries. An event data store can include events that you have logged on your account from the last 90 to 2555 days (about three months to up to seven years).
 */
export class EventDataStore extends pulumi.CustomResource {
    /**
     * Get an existing EventDataStore resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): EventDataStore {
        return new EventDataStore(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cloudtrail:EventDataStore';

    /**
     * Returns true if the given object is an instance of EventDataStore.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is EventDataStore {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === EventDataStore.__pulumiType;
    }

    /**
     * The advanced event selectors that were used to select events for the data store.
     */
    public readonly advancedEventSelectors!: pulumi.Output<outputs.cloudtrail.EventDataStoreAdvancedEventSelector[] | undefined>;
    /**
     * The timestamp of the event data store's creation.
     */
    public /*out*/ readonly createdTimestamp!: pulumi.Output<string>;
    /**
     * The ARN of the event data store.
     */
    public /*out*/ readonly eventDataStoreArn!: pulumi.Output<string>;
    /**
     * Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
     */
    public readonly kmsKeyId!: pulumi.Output<string | undefined>;
    /**
     * Indicates whether the event data store includes events from all regions, or only from the region in which it was created.
     */
    public readonly multiRegionEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The name of the event data store.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * Indicates that an event data store is collecting logged events for an organization.
     */
    public readonly organizationEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The retention period, in days.
     */
    public readonly retentionPeriod!: pulumi.Output<number | undefined>;
    /**
     * The status of an event data store. Values are ENABLED and PENDING_DELETION.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.cloudtrail.EventDataStoreTag[] | undefined>;
    /**
     * Indicates whether the event data store is protected from termination.
     */
    public readonly terminationProtectionEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The timestamp showing when an event data store was updated, if applicable. UpdatedTimestamp is always either the same or newer than the time shown in CreatedTimestamp.
     */
    public /*out*/ readonly updatedTimestamp!: pulumi.Output<string>;

    /**
     * Create a EventDataStore resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: EventDataStoreArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["advancedEventSelectors"] = args ? args.advancedEventSelectors : undefined;
            resourceInputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            resourceInputs["multiRegionEnabled"] = args ? args.multiRegionEnabled : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["organizationEnabled"] = args ? args.organizationEnabled : undefined;
            resourceInputs["retentionPeriod"] = args ? args.retentionPeriod : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["terminationProtectionEnabled"] = args ? args.terminationProtectionEnabled : undefined;
            resourceInputs["createdTimestamp"] = undefined /*out*/;
            resourceInputs["eventDataStoreArn"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["updatedTimestamp"] = undefined /*out*/;
        } else {
            resourceInputs["advancedEventSelectors"] = undefined /*out*/;
            resourceInputs["createdTimestamp"] = undefined /*out*/;
            resourceInputs["eventDataStoreArn"] = undefined /*out*/;
            resourceInputs["kmsKeyId"] = undefined /*out*/;
            resourceInputs["multiRegionEnabled"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["organizationEnabled"] = undefined /*out*/;
            resourceInputs["retentionPeriod"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["terminationProtectionEnabled"] = undefined /*out*/;
            resourceInputs["updatedTimestamp"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(EventDataStore.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a EventDataStore resource.
 */
export interface EventDataStoreArgs {
    /**
     * The advanced event selectors that were used to select events for the data store.
     */
    advancedEventSelectors?: pulumi.Input<pulumi.Input<inputs.cloudtrail.EventDataStoreAdvancedEventSelectorArgs>[]>;
    /**
     * Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
     */
    kmsKeyId?: pulumi.Input<string>;
    /**
     * Indicates whether the event data store includes events from all regions, or only from the region in which it was created.
     */
    multiRegionEnabled?: pulumi.Input<boolean>;
    /**
     * The name of the event data store.
     */
    name?: pulumi.Input<string>;
    /**
     * Indicates that an event data store is collecting logged events for an organization.
     */
    organizationEnabled?: pulumi.Input<boolean>;
    /**
     * The retention period, in days.
     */
    retentionPeriod?: pulumi.Input<number>;
    tags?: pulumi.Input<pulumi.Input<inputs.cloudtrail.EventDataStoreTagArgs>[]>;
    /**
     * Indicates whether the event data store is protected from termination.
     */
    terminationProtectionEnabled?: pulumi.Input<boolean>;
}
