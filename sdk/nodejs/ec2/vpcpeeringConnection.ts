// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::VPCPeeringConnection
 */
export class VPCPeeringConnection extends pulumi.CustomResource {
    /**
     * Get an existing VPCPeeringConnection resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VPCPeeringConnection {
        return new VPCPeeringConnection(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:VPCPeeringConnection';

    /**
     * Returns true if the given object is an instance of VPCPeeringConnection.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VPCPeeringConnection {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VPCPeeringConnection.__pulumiType;
    }

    /**
     * The AWS account ID of the owner of the accepter VPC.
     */
    public readonly peerOwnerId!: pulumi.Output<string | undefined>;
    /**
     * The Region code for the accepter VPC, if the accepter VPC is located in a Region other than the Region in which you make the request.
     */
    public readonly peerRegion!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the VPC peer role for the peering connection in another AWS account.
     */
    public readonly peerRoleArn!: pulumi.Output<string | undefined>;
    /**
     * The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request.
     */
    public readonly peerVpcId!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.ec2.VPCPeeringConnectionTag[] | undefined>;
    /**
     * The ID of the VPC.
     */
    public readonly vpcId!: pulumi.Output<string>;

    /**
     * Create a VPCPeeringConnection resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VPCPeeringConnectionArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.peerVpcId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerVpcId'");
            }
            if ((!args || args.vpcId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcId'");
            }
            resourceInputs["peerOwnerId"] = args ? args.peerOwnerId : undefined;
            resourceInputs["peerRegion"] = args ? args.peerRegion : undefined;
            resourceInputs["peerRoleArn"] = args ? args.peerRoleArn : undefined;
            resourceInputs["peerVpcId"] = args ? args.peerVpcId : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["vpcId"] = args ? args.vpcId : undefined;
        } else {
            resourceInputs["peerOwnerId"] = undefined /*out*/;
            resourceInputs["peerRegion"] = undefined /*out*/;
            resourceInputs["peerRoleArn"] = undefined /*out*/;
            resourceInputs["peerVpcId"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["vpcId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(VPCPeeringConnection.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a VPCPeeringConnection resource.
 */
export interface VPCPeeringConnectionArgs {
    /**
     * The AWS account ID of the owner of the accepter VPC.
     */
    peerOwnerId?: pulumi.Input<string>;
    /**
     * The Region code for the accepter VPC, if the accepter VPC is located in a Region other than the Region in which you make the request.
     */
    peerRegion?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) of the VPC peer role for the peering connection in another AWS account.
     */
    peerRoleArn?: pulumi.Input<string>;
    /**
     * The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request.
     */
    peerVpcId: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.VPCPeeringConnectionTagArgs>[]>;
    /**
     * The ID of the VPC.
     */
    vpcId: pulumi.Input<string>;
}
