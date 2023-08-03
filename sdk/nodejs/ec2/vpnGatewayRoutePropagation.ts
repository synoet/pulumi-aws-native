// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::VPNGatewayRoutePropagation
 *
 * @deprecated VpnGatewayRoutePropagation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class VpnGatewayRoutePropagation extends pulumi.CustomResource {
    /**
     * Get an existing VpnGatewayRoutePropagation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VpnGatewayRoutePropagation {
        pulumi.log.warn("VpnGatewayRoutePropagation is deprecated: VpnGatewayRoutePropagation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new VpnGatewayRoutePropagation(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:VpnGatewayRoutePropagation';

    /**
     * Returns true if the given object is an instance of VpnGatewayRoutePropagation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VpnGatewayRoutePropagation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VpnGatewayRoutePropagation.__pulumiType;
    }

    public readonly routeTableIds!: pulumi.Output<string[]>;
    public readonly vpnGatewayId!: pulumi.Output<string>;

    /**
     * Create a VpnGatewayRoutePropagation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated VpnGatewayRoutePropagation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: VpnGatewayRoutePropagationArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("VpnGatewayRoutePropagation is deprecated: VpnGatewayRoutePropagation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.routeTableIds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'routeTableIds'");
            }
            if ((!args || args.vpnGatewayId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpnGatewayId'");
            }
            resourceInputs["routeTableIds"] = args ? args.routeTableIds : undefined;
            resourceInputs["vpnGatewayId"] = args ? args.vpnGatewayId : undefined;
        } else {
            resourceInputs["routeTableIds"] = undefined /*out*/;
            resourceInputs["vpnGatewayId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(VpnGatewayRoutePropagation.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a VpnGatewayRoutePropagation resource.
 */
export interface VpnGatewayRoutePropagationArgs {
    routeTableIds: pulumi.Input<pulumi.Input<string>[]>;
    vpnGatewayId: pulumi.Input<string>;
}
