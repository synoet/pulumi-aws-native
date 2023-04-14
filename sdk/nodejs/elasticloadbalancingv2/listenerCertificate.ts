// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElasticLoadBalancingV2::ListenerCertificate
 *
 * @deprecated ListenerCertificate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class ListenerCertificate extends pulumi.CustomResource {
    /**
     * Get an existing ListenerCertificate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ListenerCertificate {
        pulumi.log.warn("ListenerCertificate is deprecated: ListenerCertificate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new ListenerCertificate(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:elasticloadbalancingv2:ListenerCertificate';

    /**
     * Returns true if the given object is an instance of ListenerCertificate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ListenerCertificate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ListenerCertificate.__pulumiType;
    }

    public readonly certificates!: pulumi.Output<outputs.elasticloadbalancingv2.ListenerCertificateCertificate[]>;
    public readonly listenerArn!: pulumi.Output<string>;

    /**
     * Create a ListenerCertificate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated ListenerCertificate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ListenerCertificateArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ListenerCertificate is deprecated: ListenerCertificate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.certificates === undefined) && !opts.urn) {
                throw new Error("Missing required property 'certificates'");
            }
            if ((!args || args.listenerArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'listenerArn'");
            }
            resourceInputs["certificates"] = args ? args.certificates : undefined;
            resourceInputs["listenerArn"] = args ? args.listenerArn : undefined;
        } else {
            resourceInputs["certificates"] = undefined /*out*/;
            resourceInputs["listenerArn"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ListenerCertificate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ListenerCertificate resource.
 */
export interface ListenerCertificateArgs {
    certificates: pulumi.Input<pulumi.Input<inputs.elasticloadbalancingv2.ListenerCertificateCertificateArgs>[]>;
    listenerArn: pulumi.Input<string>;
}
