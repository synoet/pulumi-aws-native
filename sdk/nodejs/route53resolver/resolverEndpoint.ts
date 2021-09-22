// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Route53Resolver::ResolverEndpoint
 *
 * @deprecated ResolverEndpoint is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class ResolverEndpoint extends pulumi.CustomResource {
    /**
     * Get an existing ResolverEndpoint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ResolverEndpoint {
        pulumi.log.warn("ResolverEndpoint is deprecated: ResolverEndpoint is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new ResolverEndpoint(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:route53resolver:ResolverEndpoint';

    /**
     * Returns true if the given object is an instance of ResolverEndpoint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ResolverEndpoint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ResolverEndpoint.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly direction!: pulumi.Output<string>;
    public /*out*/ readonly hostVPCId!: pulumi.Output<string>;
    public /*out*/ readonly ipAddressCount!: pulumi.Output<string>;
    public readonly ipAddresses!: pulumi.Output<outputs.route53resolver.ResolverEndpointIpAddressRequest[]>;
    public readonly name!: pulumi.Output<string | undefined>;
    public /*out*/ readonly resolverEndpointId!: pulumi.Output<string>;
    public readonly securityGroupIds!: pulumi.Output<string[]>;
    public readonly tags!: pulumi.Output<outputs.route53resolver.ResolverEndpointTag[] | undefined>;

    /**
     * Create a ResolverEndpoint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated ResolverEndpoint is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ResolverEndpointArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ResolverEndpoint is deprecated: ResolverEndpoint is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.direction === undefined) && !opts.urn) {
                throw new Error("Missing required property 'direction'");
            }
            if ((!args || args.ipAddresses === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ipAddresses'");
            }
            if ((!args || args.securityGroupIds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'securityGroupIds'");
            }
            inputs["direction"] = args ? args.direction : undefined;
            inputs["ipAddresses"] = args ? args.ipAddresses : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["securityGroupIds"] = args ? args.securityGroupIds : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["hostVPCId"] = undefined /*out*/;
            inputs["ipAddressCount"] = undefined /*out*/;
            inputs["resolverEndpointId"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["direction"] = undefined /*out*/;
            inputs["hostVPCId"] = undefined /*out*/;
            inputs["ipAddressCount"] = undefined /*out*/;
            inputs["ipAddresses"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["resolverEndpointId"] = undefined /*out*/;
            inputs["securityGroupIds"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ResolverEndpoint.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ResolverEndpoint resource.
 */
export interface ResolverEndpointArgs {
    direction: pulumi.Input<string>;
    ipAddresses: pulumi.Input<pulumi.Input<inputs.route53resolver.ResolverEndpointIpAddressRequestArgs>[]>;
    name?: pulumi.Input<string>;
    securityGroupIds: pulumi.Input<pulumi.Input<string>[]>;
    tags?: pulumi.Input<pulumi.Input<inputs.route53resolver.ResolverEndpointTagArgs>[]>;
}
