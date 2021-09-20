// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::MediaConnect::FlowEntitlement
 */
export class FlowEntitlement extends pulumi.CustomResource {
    /**
     * Get an existing FlowEntitlement resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): FlowEntitlement {
        return new FlowEntitlement(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:mediaconnect:FlowEntitlement';

    /**
     * Returns true if the given object is an instance of FlowEntitlement.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FlowEntitlement {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FlowEntitlement.__pulumiType;
    }

    /**
     * Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
     */
    public readonly dataTransferSubscriberFeePercent!: pulumi.Output<number | undefined>;
    /**
     * A description of the entitlement.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The type of encryption that will be used on the output that is associated with this entitlement.
     */
    public readonly encryption!: pulumi.Output<outputs.mediaconnect.FlowEntitlementEncryption | undefined>;
    /**
     * The ARN of the entitlement.
     */
    public /*out*/ readonly entitlementArn!: pulumi.Output<string>;
    /**
     *  An indication of whether the entitlement is enabled.
     */
    public readonly entitlementStatus!: pulumi.Output<enums.mediaconnect.FlowEntitlementEntitlementStatus | undefined>;
    /**
     * The ARN of the flow.
     */
    public readonly flowArn!: pulumi.Output<string>;
    /**
     * The name of the entitlement.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
     */
    public readonly subscribers!: pulumi.Output<string[]>;

    /**
     * Create a FlowEntitlement resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FlowEntitlementArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            if ((!args || args.flowArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'flowArn'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.subscribers === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subscribers'");
            }
            inputs["dataTransferSubscriberFeePercent"] = args ? args.dataTransferSubscriberFeePercent : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["encryption"] = args ? args.encryption : undefined;
            inputs["entitlementStatus"] = args ? args.entitlementStatus : undefined;
            inputs["flowArn"] = args ? args.flowArn : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["subscribers"] = args ? args.subscribers : undefined;
            inputs["entitlementArn"] = undefined /*out*/;
        } else {
            inputs["dataTransferSubscriberFeePercent"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["encryption"] = undefined /*out*/;
            inputs["entitlementArn"] = undefined /*out*/;
            inputs["entitlementStatus"] = undefined /*out*/;
            inputs["flowArn"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["subscribers"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(FlowEntitlement.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a FlowEntitlement resource.
 */
export interface FlowEntitlementArgs {
    /**
     * Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
     */
    dataTransferSubscriberFeePercent?: pulumi.Input<number>;
    /**
     * A description of the entitlement.
     */
    description: pulumi.Input<string>;
    /**
     * The type of encryption that will be used on the output that is associated with this entitlement.
     */
    encryption?: pulumi.Input<inputs.mediaconnect.FlowEntitlementEncryptionArgs>;
    /**
     *  An indication of whether the entitlement is enabled.
     */
    entitlementStatus?: pulumi.Input<enums.mediaconnect.FlowEntitlementEntitlementStatus>;
    /**
     * The ARN of the flow.
     */
    flowArn: pulumi.Input<string>;
    /**
     * The name of the entitlement.
     */
    name: pulumi.Input<string>;
    /**
     * The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
     */
    subscribers: pulumi.Input<pulumi.Input<string>[]>;
}
