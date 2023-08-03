// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::VPC
 */
export class Vpc extends pulumi.CustomResource {
    /**
     * Get an existing Vpc resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Vpc {
        return new Vpc(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:Vpc';

    /**
     * Returns true if the given object is an instance of Vpc.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Vpc {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Vpc.__pulumiType;
    }

    /**
     * The primary IPv4 CIDR block for the VPC.
     */
    public readonly cidrBlock!: pulumi.Output<string | undefined>;
    /**
     * A list of IPv4 CIDR block association IDs for the VPC.
     */
    public /*out*/ readonly cidrBlockAssociations!: pulumi.Output<string[]>;
    /**
     * The default network ACL ID that is associated with the VPC.
     */
    public /*out*/ readonly defaultNetworkAcl!: pulumi.Output<string>;
    /**
     * The default security group ID that is associated with the VPC.
     */
    public /*out*/ readonly defaultSecurityGroup!: pulumi.Output<string>;
    /**
     * Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not. Disabled by default for nondefault VPCs.
     */
    public readonly enableDnsHostnames!: pulumi.Output<boolean | undefined>;
    /**
     * Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled. Enabled by default.
     */
    public readonly enableDnsSupport!: pulumi.Output<boolean | undefined>;
    /**
     * The allowed tenancy of instances launched into the VPC.
     *
     * "default": An instance launched into the VPC runs on shared hardware by default, unless you explicitly specify a different tenancy during instance launch.
     *
     * "dedicated": An instance launched into the VPC is a Dedicated Instance by default, unless you explicitly specify a tenancy of host during instance launch. You cannot specify a tenancy of default during instance launch.
     *
     * Updating InstanceTenancy requires no replacement only if you are updating its value from "dedicated" to "default". Updating InstanceTenancy from "default" to "dedicated" requires replacement.
     */
    public readonly instanceTenancy!: pulumi.Output<string | undefined>;
    /**
     * The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR
     */
    public readonly ipv4IpamPoolId!: pulumi.Output<string | undefined>;
    /**
     * The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool
     */
    public readonly ipv4NetmaskLength!: pulumi.Output<number | undefined>;
    /**
     * A list of IPv6 CIDR blocks that are associated with the VPC.
     */
    public /*out*/ readonly ipv6CidrBlocks!: pulumi.Output<string[]>;
    /**
     * The tags for the VPC.
     */
    public readonly tags!: pulumi.Output<outputs.ec2.VpcTag[] | undefined>;
    /**
     * The Id for the model.
     */
    public /*out*/ readonly vpcId!: pulumi.Output<string>;

    /**
     * Create a Vpc resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: VpcArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["cidrBlock"] = args ? args.cidrBlock : undefined;
            resourceInputs["enableDnsHostnames"] = args ? args.enableDnsHostnames : undefined;
            resourceInputs["enableDnsSupport"] = args ? args.enableDnsSupport : undefined;
            resourceInputs["instanceTenancy"] = args ? args.instanceTenancy : undefined;
            resourceInputs["ipv4IpamPoolId"] = args ? args.ipv4IpamPoolId : undefined;
            resourceInputs["ipv4NetmaskLength"] = args ? args.ipv4NetmaskLength : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["cidrBlockAssociations"] = undefined /*out*/;
            resourceInputs["defaultNetworkAcl"] = undefined /*out*/;
            resourceInputs["defaultSecurityGroup"] = undefined /*out*/;
            resourceInputs["ipv6CidrBlocks"] = undefined /*out*/;
            resourceInputs["vpcId"] = undefined /*out*/;
        } else {
            resourceInputs["cidrBlock"] = undefined /*out*/;
            resourceInputs["cidrBlockAssociations"] = undefined /*out*/;
            resourceInputs["defaultNetworkAcl"] = undefined /*out*/;
            resourceInputs["defaultSecurityGroup"] = undefined /*out*/;
            resourceInputs["enableDnsHostnames"] = undefined /*out*/;
            resourceInputs["enableDnsSupport"] = undefined /*out*/;
            resourceInputs["instanceTenancy"] = undefined /*out*/;
            resourceInputs["ipv4IpamPoolId"] = undefined /*out*/;
            resourceInputs["ipv4NetmaskLength"] = undefined /*out*/;
            resourceInputs["ipv6CidrBlocks"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["vpcId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Vpc.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Vpc resource.
 */
export interface VpcArgs {
    /**
     * The primary IPv4 CIDR block for the VPC.
     */
    cidrBlock?: pulumi.Input<string>;
    /**
     * Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not. Disabled by default for nondefault VPCs.
     */
    enableDnsHostnames?: pulumi.Input<boolean>;
    /**
     * Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled. Enabled by default.
     */
    enableDnsSupport?: pulumi.Input<boolean>;
    /**
     * The allowed tenancy of instances launched into the VPC.
     *
     * "default": An instance launched into the VPC runs on shared hardware by default, unless you explicitly specify a different tenancy during instance launch.
     *
     * "dedicated": An instance launched into the VPC is a Dedicated Instance by default, unless you explicitly specify a tenancy of host during instance launch. You cannot specify a tenancy of default during instance launch.
     *
     * Updating InstanceTenancy requires no replacement only if you are updating its value from "dedicated" to "default". Updating InstanceTenancy from "default" to "dedicated" requires replacement.
     */
    instanceTenancy?: pulumi.Input<string>;
    /**
     * The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR
     */
    ipv4IpamPoolId?: pulumi.Input<string>;
    /**
     * The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool
     */
    ipv4NetmaskLength?: pulumi.Input<number>;
    /**
     * The tags for the VPC.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.VpcTagArgs>[]>;
}
