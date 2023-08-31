// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The AWS::NetworkManager::CustomerGatewayAssociation type associates a customer gateway with a device and optionally, with a link.
 */
export class CustomerGatewayAssociation extends pulumi.CustomResource {
    /**
     * Get an existing CustomerGatewayAssociation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): CustomerGatewayAssociation {
        return new CustomerGatewayAssociation(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:networkmanager:CustomerGatewayAssociation';

    /**
     * Returns true if the given object is an instance of CustomerGatewayAssociation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CustomerGatewayAssociation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CustomerGatewayAssociation.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the customer gateway.
     */
    public readonly customerGatewayArn!: pulumi.Output<string>;
    /**
     * The ID of the device
     */
    public readonly deviceId!: pulumi.Output<string>;
    /**
     * The ID of the global network.
     */
    public readonly globalNetworkId!: pulumi.Output<string>;
    /**
     * The ID of the link
     */
    public readonly linkId!: pulumi.Output<string | undefined>;

    /**
     * Create a CustomerGatewayAssociation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CustomerGatewayAssociationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.customerGatewayArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'customerGatewayArn'");
            }
            if ((!args || args.deviceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'deviceId'");
            }
            if ((!args || args.globalNetworkId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'globalNetworkId'");
            }
            resourceInputs["customerGatewayArn"] = args ? args.customerGatewayArn : undefined;
            resourceInputs["deviceId"] = args ? args.deviceId : undefined;
            resourceInputs["globalNetworkId"] = args ? args.globalNetworkId : undefined;
            resourceInputs["linkId"] = args ? args.linkId : undefined;
        } else {
            resourceInputs["customerGatewayArn"] = undefined /*out*/;
            resourceInputs["deviceId"] = undefined /*out*/;
            resourceInputs["globalNetworkId"] = undefined /*out*/;
            resourceInputs["linkId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["customerGatewayArn", "deviceId", "globalNetworkId", "linkId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(CustomerGatewayAssociation.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a CustomerGatewayAssociation resource.
 */
export interface CustomerGatewayAssociationArgs {
    /**
     * The Amazon Resource Name (ARN) of the customer gateway.
     */
    customerGatewayArn: pulumi.Input<string>;
    /**
     * The ID of the device
     */
    deviceId: pulumi.Input<string>;
    /**
     * The ID of the global network.
     */
    globalNetworkId: pulumi.Input<string>;
    /**
     * The ID of the link
     */
    linkId?: pulumi.Input<string>;
}
