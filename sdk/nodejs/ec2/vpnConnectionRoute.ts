// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::VPNConnectionRoute
 */
export class VpnConnectionRoute extends pulumi.CustomResource {
    /**
     * Get an existing VpnConnectionRoute resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VpnConnectionRoute {
        return new VpnConnectionRoute(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:VpnConnectionRoute';

    /**
     * Returns true if the given object is an instance of VpnConnectionRoute.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VpnConnectionRoute {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VpnConnectionRoute.__pulumiType;
    }

    /**
     * The CIDR block associated with the local subnet of the customer network.
     */
    public readonly destinationCidrBlock!: pulumi.Output<string>;
    /**
     * The ID of the VPN connection.
     */
    public readonly vpnConnectionId!: pulumi.Output<string>;

    /**
     * Create a VpnConnectionRoute resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VpnConnectionRouteArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.destinationCidrBlock === undefined) && !opts.urn) {
                throw new Error("Missing required property 'destinationCidrBlock'");
            }
            if ((!args || args.vpnConnectionId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpnConnectionId'");
            }
            resourceInputs["destinationCidrBlock"] = args ? args.destinationCidrBlock : undefined;
            resourceInputs["vpnConnectionId"] = args ? args.vpnConnectionId : undefined;
        } else {
            resourceInputs["destinationCidrBlock"] = undefined /*out*/;
            resourceInputs["vpnConnectionId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(VpnConnectionRoute.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a VpnConnectionRoute resource.
 */
export interface VpnConnectionRouteArgs {
    /**
     * The CIDR block associated with the local subnet of the customer network.
     */
    destinationCidrBlock: pulumi.Input<string>;
    /**
     * The ID of the VPN connection.
     */
    vpnConnectionId: pulumi.Input<string>;
}
