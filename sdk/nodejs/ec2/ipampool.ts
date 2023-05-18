// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Schema of AWS::EC2::IPAMPool Type
 */
export class IPAMPool extends pulumi.CustomResource {
    /**
     * Get an existing IPAMPool resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): IPAMPool {
        return new IPAMPool(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:IPAMPool';

    /**
     * Returns true if the given object is an instance of IPAMPool.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IPAMPool {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IPAMPool.__pulumiType;
    }

    /**
     * The address family of the address space in this pool. Either IPv4 or IPv6.
     */
    public readonly addressFamily!: pulumi.Output<string>;
    /**
     * The default netmask length for allocations made from this pool. This value is used when the netmask length of an allocation isn't specified.
     */
    public readonly allocationDefaultNetmaskLength!: pulumi.Output<number | undefined>;
    /**
     * The maximum allowed netmask length for allocations made from this pool.
     */
    public readonly allocationMaxNetmaskLength!: pulumi.Output<number | undefined>;
    /**
     * The minimum allowed netmask length for allocations made from this pool.
     */
    public readonly allocationMinNetmaskLength!: pulumi.Output<number | undefined>;
    /**
     * When specified, an allocation will not be allowed unless a resource has a matching set of tags.
     */
    public readonly allocationResourceTags!: pulumi.Output<outputs.ec2.IPAMPoolTag[] | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the IPAM Pool.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Determines what to do if IPAM discovers resources that haven't been assigned an allocation. If set to true, an allocation will be made automatically.
     */
    public readonly autoImport!: pulumi.Output<boolean | undefined>;
    /**
     * Limits which service in Amazon Web Services that the pool can be used in.
     */
    public readonly awsService!: pulumi.Output<enums.ec2.IPAMPoolAwsService | undefined>;
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the IPAM this pool is a part of.
     */
    public /*out*/ readonly ipamArn!: pulumi.Output<string>;
    /**
     * Id of the IPAM Pool.
     */
    public /*out*/ readonly ipamPoolId!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) of the scope this pool is a part of.
     */
    public /*out*/ readonly ipamScopeArn!: pulumi.Output<string>;
    /**
     * The Id of the scope this pool is a part of.
     */
    public readonly ipamScopeId!: pulumi.Output<string>;
    /**
     * Determines whether this scope contains publicly routable space or space for a private network
     */
    public /*out*/ readonly ipamScopeType!: pulumi.Output<enums.ec2.IPAMPoolIpamScopeType>;
    /**
     * The region of this pool. If not set, this will default to "None" which will disable non-custom allocations. If the locale has been specified for the source pool, this value must match.
     */
    public readonly locale!: pulumi.Output<string | undefined>;
    /**
     * The depth of this pool in the source pool hierarchy.
     */
    public /*out*/ readonly poolDepth!: pulumi.Output<number>;
    /**
     * A list of cidrs representing the address space available for allocation in this pool.
     */
    public readonly provisionedCidrs!: pulumi.Output<outputs.ec2.IPAMPoolProvisionedCidr[] | undefined>;
    /**
     * The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `byoip`.
     */
    public readonly publicIpSource!: pulumi.Output<enums.ec2.IPAMPoolPublicIpSource | undefined>;
    /**
     * Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.
     */
    public readonly publiclyAdvertisable!: pulumi.Output<boolean | undefined>;
    /**
     * The Id of this pool's source. If set, all space provisioned in this pool must be free space provisioned in the parent pool.
     */
    public readonly sourceIpamPoolId!: pulumi.Output<string | undefined>;
    /**
     * The state of this pool. This can be one of the following values: "create-in-progress", "create-complete", "modify-in-progress", "modify-complete", "delete-in-progress", or "delete-complete"
     */
    public /*out*/ readonly state!: pulumi.Output<enums.ec2.IPAMPoolState>;
    /**
     * An explanation of how the pool arrived at it current state.
     */
    public /*out*/ readonly stateMessage!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.ec2.IPAMPoolTag[] | undefined>;

    /**
     * Create a IPAMPool resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IPAMPoolArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.addressFamily === undefined) && !opts.urn) {
                throw new Error("Missing required property 'addressFamily'");
            }
            if ((!args || args.ipamScopeId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ipamScopeId'");
            }
            resourceInputs["addressFamily"] = args ? args.addressFamily : undefined;
            resourceInputs["allocationDefaultNetmaskLength"] = args ? args.allocationDefaultNetmaskLength : undefined;
            resourceInputs["allocationMaxNetmaskLength"] = args ? args.allocationMaxNetmaskLength : undefined;
            resourceInputs["allocationMinNetmaskLength"] = args ? args.allocationMinNetmaskLength : undefined;
            resourceInputs["allocationResourceTags"] = args ? args.allocationResourceTags : undefined;
            resourceInputs["autoImport"] = args ? args.autoImport : undefined;
            resourceInputs["awsService"] = args ? args.awsService : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["ipamScopeId"] = args ? args.ipamScopeId : undefined;
            resourceInputs["locale"] = args ? args.locale : undefined;
            resourceInputs["provisionedCidrs"] = args ? args.provisionedCidrs : undefined;
            resourceInputs["publicIpSource"] = args ? args.publicIpSource : undefined;
            resourceInputs["publiclyAdvertisable"] = args ? args.publiclyAdvertisable : undefined;
            resourceInputs["sourceIpamPoolId"] = args ? args.sourceIpamPoolId : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["ipamArn"] = undefined /*out*/;
            resourceInputs["ipamPoolId"] = undefined /*out*/;
            resourceInputs["ipamScopeArn"] = undefined /*out*/;
            resourceInputs["ipamScopeType"] = undefined /*out*/;
            resourceInputs["poolDepth"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["stateMessage"] = undefined /*out*/;
        } else {
            resourceInputs["addressFamily"] = undefined /*out*/;
            resourceInputs["allocationDefaultNetmaskLength"] = undefined /*out*/;
            resourceInputs["allocationMaxNetmaskLength"] = undefined /*out*/;
            resourceInputs["allocationMinNetmaskLength"] = undefined /*out*/;
            resourceInputs["allocationResourceTags"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["autoImport"] = undefined /*out*/;
            resourceInputs["awsService"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["ipamArn"] = undefined /*out*/;
            resourceInputs["ipamPoolId"] = undefined /*out*/;
            resourceInputs["ipamScopeArn"] = undefined /*out*/;
            resourceInputs["ipamScopeId"] = undefined /*out*/;
            resourceInputs["ipamScopeType"] = undefined /*out*/;
            resourceInputs["locale"] = undefined /*out*/;
            resourceInputs["poolDepth"] = undefined /*out*/;
            resourceInputs["provisionedCidrs"] = undefined /*out*/;
            resourceInputs["publicIpSource"] = undefined /*out*/;
            resourceInputs["publiclyAdvertisable"] = undefined /*out*/;
            resourceInputs["sourceIpamPoolId"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["stateMessage"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(IPAMPool.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a IPAMPool resource.
 */
export interface IPAMPoolArgs {
    /**
     * The address family of the address space in this pool. Either IPv4 or IPv6.
     */
    addressFamily: pulumi.Input<string>;
    /**
     * The default netmask length for allocations made from this pool. This value is used when the netmask length of an allocation isn't specified.
     */
    allocationDefaultNetmaskLength?: pulumi.Input<number>;
    /**
     * The maximum allowed netmask length for allocations made from this pool.
     */
    allocationMaxNetmaskLength?: pulumi.Input<number>;
    /**
     * The minimum allowed netmask length for allocations made from this pool.
     */
    allocationMinNetmaskLength?: pulumi.Input<number>;
    /**
     * When specified, an allocation will not be allowed unless a resource has a matching set of tags.
     */
    allocationResourceTags?: pulumi.Input<pulumi.Input<inputs.ec2.IPAMPoolTagArgs>[]>;
    /**
     * Determines what to do if IPAM discovers resources that haven't been assigned an allocation. If set to true, an allocation will be made automatically.
     */
    autoImport?: pulumi.Input<boolean>;
    /**
     * Limits which service in Amazon Web Services that the pool can be used in.
     */
    awsService?: pulumi.Input<enums.ec2.IPAMPoolAwsService>;
    description?: pulumi.Input<string>;
    /**
     * The Id of the scope this pool is a part of.
     */
    ipamScopeId: pulumi.Input<string>;
    /**
     * The region of this pool. If not set, this will default to "None" which will disable non-custom allocations. If the locale has been specified for the source pool, this value must match.
     */
    locale?: pulumi.Input<string>;
    /**
     * A list of cidrs representing the address space available for allocation in this pool.
     */
    provisionedCidrs?: pulumi.Input<pulumi.Input<inputs.ec2.IPAMPoolProvisionedCidrArgs>[]>;
    /**
     * The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `byoip`.
     */
    publicIpSource?: pulumi.Input<enums.ec2.IPAMPoolPublicIpSource>;
    /**
     * Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.
     */
    publiclyAdvertisable?: pulumi.Input<boolean>;
    /**
     * The Id of this pool's source. If set, all space provisioned in this pool must be free space provisioned in the parent pool.
     */
    sourceIpamPoolId?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.IPAMPoolTagArgs>[]>;
}
