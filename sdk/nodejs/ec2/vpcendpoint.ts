// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::VPCEndpoint
 *
 * @deprecated VPCEndpoint is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class VPCEndpoint extends pulumi.CustomResource {
    /**
     * Get an existing VPCEndpoint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VPCEndpoint {
        pulumi.log.warn("VPCEndpoint is deprecated: VPCEndpoint is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new VPCEndpoint(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:VPCEndpoint';

    /**
     * Returns true if the given object is an instance of VPCEndpoint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VPCEndpoint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VPCEndpoint.__pulumiType;
    }

    public /*out*/ readonly creationTimestamp!: pulumi.Output<string>;
    public /*out*/ readonly dnsEntries!: pulumi.Output<string[]>;
    public /*out*/ readonly networkInterfaceIds!: pulumi.Output<string[]>;
    public readonly policyDocument!: pulumi.Output<any | undefined>;
    public readonly privateDnsEnabled!: pulumi.Output<boolean | undefined>;
    public readonly routeTableIds!: pulumi.Output<string[] | undefined>;
    public readonly securityGroupIds!: pulumi.Output<string[] | undefined>;
    public readonly serviceName!: pulumi.Output<string>;
    public readonly subnetIds!: pulumi.Output<string[] | undefined>;
    public readonly vpcEndpointType!: pulumi.Output<string | undefined>;
    public readonly vpcId!: pulumi.Output<string>;

    /**
     * Create a VPCEndpoint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated VPCEndpoint is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: VPCEndpointArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("VPCEndpoint is deprecated: VPCEndpoint is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            if ((!args || args.vpcId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcId'");
            }
            inputs["policyDocument"] = args ? args.policyDocument : undefined;
            inputs["privateDnsEnabled"] = args ? args.privateDnsEnabled : undefined;
            inputs["routeTableIds"] = args ? args.routeTableIds : undefined;
            inputs["securityGroupIds"] = args ? args.securityGroupIds : undefined;
            inputs["serviceName"] = args ? args.serviceName : undefined;
            inputs["subnetIds"] = args ? args.subnetIds : undefined;
            inputs["vpcEndpointType"] = args ? args.vpcEndpointType : undefined;
            inputs["vpcId"] = args ? args.vpcId : undefined;
            inputs["creationTimestamp"] = undefined /*out*/;
            inputs["dnsEntries"] = undefined /*out*/;
            inputs["networkInterfaceIds"] = undefined /*out*/;
        } else {
            inputs["creationTimestamp"] = undefined /*out*/;
            inputs["dnsEntries"] = undefined /*out*/;
            inputs["networkInterfaceIds"] = undefined /*out*/;
            inputs["policyDocument"] = undefined /*out*/;
            inputs["privateDnsEnabled"] = undefined /*out*/;
            inputs["routeTableIds"] = undefined /*out*/;
            inputs["securityGroupIds"] = undefined /*out*/;
            inputs["serviceName"] = undefined /*out*/;
            inputs["subnetIds"] = undefined /*out*/;
            inputs["vpcEndpointType"] = undefined /*out*/;
            inputs["vpcId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(VPCEndpoint.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a VPCEndpoint resource.
 */
export interface VPCEndpointArgs {
    policyDocument?: any;
    privateDnsEnabled?: pulumi.Input<boolean>;
    routeTableIds?: pulumi.Input<pulumi.Input<string>[]>;
    securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    serviceName: pulumi.Input<string>;
    subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
    vpcEndpointType?: pulumi.Input<string>;
    vpcId: pulumi.Input<string>;
}
