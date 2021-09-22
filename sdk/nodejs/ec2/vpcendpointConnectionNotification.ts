// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::VPCEndpointConnectionNotification
 *
 * @deprecated VPCEndpointConnectionNotification is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class VPCEndpointConnectionNotification extends pulumi.CustomResource {
    /**
     * Get an existing VPCEndpointConnectionNotification resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VPCEndpointConnectionNotification {
        pulumi.log.warn("VPCEndpointConnectionNotification is deprecated: VPCEndpointConnectionNotification is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new VPCEndpointConnectionNotification(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:VPCEndpointConnectionNotification';

    /**
     * Returns true if the given object is an instance of VPCEndpointConnectionNotification.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VPCEndpointConnectionNotification {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VPCEndpointConnectionNotification.__pulumiType;
    }

    public readonly connectionEvents!: pulumi.Output<string[]>;
    public readonly connectionNotificationArn!: pulumi.Output<string>;
    public readonly serviceId!: pulumi.Output<string | undefined>;
    public readonly vPCEndpointId!: pulumi.Output<string | undefined>;

    /**
     * Create a VPCEndpointConnectionNotification resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated VPCEndpointConnectionNotification is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: VPCEndpointConnectionNotificationArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("VPCEndpointConnectionNotification is deprecated: VPCEndpointConnectionNotification is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.connectionEvents === undefined) && !opts.urn) {
                throw new Error("Missing required property 'connectionEvents'");
            }
            if ((!args || args.connectionNotificationArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'connectionNotificationArn'");
            }
            inputs["connectionEvents"] = args ? args.connectionEvents : undefined;
            inputs["connectionNotificationArn"] = args ? args.connectionNotificationArn : undefined;
            inputs["serviceId"] = args ? args.serviceId : undefined;
            inputs["vPCEndpointId"] = args ? args.vPCEndpointId : undefined;
        } else {
            inputs["connectionEvents"] = undefined /*out*/;
            inputs["connectionNotificationArn"] = undefined /*out*/;
            inputs["serviceId"] = undefined /*out*/;
            inputs["vPCEndpointId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(VPCEndpointConnectionNotification.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a VPCEndpointConnectionNotification resource.
 */
export interface VPCEndpointConnectionNotificationArgs {
    connectionEvents: pulumi.Input<pulumi.Input<string>[]>;
    connectionNotificationArn: pulumi.Input<string>;
    serviceId?: pulumi.Input<string>;
    vPCEndpointId?: pulumi.Input<string>;
}
