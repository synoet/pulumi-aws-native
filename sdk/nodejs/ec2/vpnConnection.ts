// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::VPNConnection
 */
export class VpnConnection extends pulumi.CustomResource {
    /**
     * Get an existing VpnConnection resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VpnConnection {
        return new VpnConnection(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:VpnConnection';

    /**
     * Returns true if the given object is an instance of VpnConnection.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VpnConnection {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VpnConnection.__pulumiType;
    }

    /**
     * The ID of the customer gateway at your end of the VPN connection.
     */
    public readonly customerGatewayId!: pulumi.Output<string>;
    /**
     * Indicates whether the VPN connection uses static routes only.
     */
    public readonly staticRoutesOnly!: pulumi.Output<boolean | undefined>;
    /**
     * Any tags assigned to the VPN connection.
     */
    public readonly tags!: pulumi.Output<outputs.ec2.VpnConnectionTag[] | undefined>;
    /**
     * The ID of the transit gateway associated with the VPN connection.
     */
    public readonly transitGatewayId!: pulumi.Output<string | undefined>;
    /**
     * The type of VPN connection.
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * The provider-assigned unique ID for this managed resource
     */
    public /*out*/ readonly vpnConnectionId!: pulumi.Output<string>;
    /**
     * The ID of the virtual private gateway at the AWS side of the VPN connection.
     */
    public readonly vpnGatewayId!: pulumi.Output<string | undefined>;
    /**
     * The tunnel options for the VPN connection.
     */
    public readonly vpnTunnelOptionsSpecifications!: pulumi.Output<outputs.ec2.VpnConnectionVpnTunnelOptionsSpecification[] | undefined>;

    /**
     * Create a VpnConnection resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VpnConnectionArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.customerGatewayId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'customerGatewayId'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["customerGatewayId"] = args ? args.customerGatewayId : undefined;
            resourceInputs["staticRoutesOnly"] = args ? args.staticRoutesOnly : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["transitGatewayId"] = args ? args.transitGatewayId : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["vpnGatewayId"] = args ? args.vpnGatewayId : undefined;
            resourceInputs["vpnTunnelOptionsSpecifications"] = args ? args.vpnTunnelOptionsSpecifications : undefined;
            resourceInputs["vpnConnectionId"] = undefined /*out*/;
        } else {
            resourceInputs["customerGatewayId"] = undefined /*out*/;
            resourceInputs["staticRoutesOnly"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["transitGatewayId"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
            resourceInputs["vpnConnectionId"] = undefined /*out*/;
            resourceInputs["vpnGatewayId"] = undefined /*out*/;
            resourceInputs["vpnTunnelOptionsSpecifications"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(VpnConnection.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a VpnConnection resource.
 */
export interface VpnConnectionArgs {
    /**
     * The ID of the customer gateway at your end of the VPN connection.
     */
    customerGatewayId: pulumi.Input<string>;
    /**
     * Indicates whether the VPN connection uses static routes only.
     */
    staticRoutesOnly?: pulumi.Input<boolean>;
    /**
     * Any tags assigned to the VPN connection.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.VpnConnectionTagArgs>[]>;
    /**
     * The ID of the transit gateway associated with the VPN connection.
     */
    transitGatewayId?: pulumi.Input<string>;
    /**
     * The type of VPN connection.
     */
    type: pulumi.Input<string>;
    /**
     * The ID of the virtual private gateway at the AWS side of the VPN connection.
     */
    vpnGatewayId?: pulumi.Input<string>;
    /**
     * The tunnel options for the VPN connection.
     */
    vpnTunnelOptionsSpecifications?: pulumi.Input<pulumi.Input<inputs.ec2.VpnConnectionVpnTunnelOptionsSpecificationArgs>[]>;
}
