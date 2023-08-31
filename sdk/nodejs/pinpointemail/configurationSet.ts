// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::PinpointEmail::ConfigurationSet
 *
 * @deprecated ConfigurationSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class ConfigurationSet extends pulumi.CustomResource {
    /**
     * Get an existing ConfigurationSet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ConfigurationSet {
        pulumi.log.warn("ConfigurationSet is deprecated: ConfigurationSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new ConfigurationSet(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:pinpointemail:ConfigurationSet';

    /**
     * Returns true if the given object is an instance of ConfigurationSet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConfigurationSet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConfigurationSet.__pulumiType;
    }

    public readonly deliveryOptions!: pulumi.Output<outputs.pinpointemail.ConfigurationSetDeliveryOptions | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly reputationOptions!: pulumi.Output<outputs.pinpointemail.ConfigurationSetReputationOptions | undefined>;
    public readonly sendingOptions!: pulumi.Output<outputs.pinpointemail.ConfigurationSetSendingOptions | undefined>;
    public readonly tags!: pulumi.Output<outputs.pinpointemail.ConfigurationSetTags[] | undefined>;
    public readonly trackingOptions!: pulumi.Output<outputs.pinpointemail.ConfigurationSetTrackingOptions | undefined>;

    /**
     * Create a ConfigurationSet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated ConfigurationSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args?: ConfigurationSetArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ConfigurationSet is deprecated: ConfigurationSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["deliveryOptions"] = args ? args.deliveryOptions : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["reputationOptions"] = args ? args.reputationOptions : undefined;
            resourceInputs["sendingOptions"] = args ? args.sendingOptions : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["trackingOptions"] = args ? args.trackingOptions : undefined;
        } else {
            resourceInputs["deliveryOptions"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["reputationOptions"] = undefined /*out*/;
            resourceInputs["sendingOptions"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["trackingOptions"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ConfigurationSet.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ConfigurationSet resource.
 */
export interface ConfigurationSetArgs {
    deliveryOptions?: pulumi.Input<inputs.pinpointemail.ConfigurationSetDeliveryOptionsArgs>;
    name?: pulumi.Input<string>;
    reputationOptions?: pulumi.Input<inputs.pinpointemail.ConfigurationSetReputationOptionsArgs>;
    sendingOptions?: pulumi.Input<inputs.pinpointemail.ConfigurationSetSendingOptionsArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.pinpointemail.ConfigurationSetTagsArgs>[]>;
    trackingOptions?: pulumi.Input<inputs.pinpointemail.ConfigurationSetTrackingOptionsArgs>;
}
