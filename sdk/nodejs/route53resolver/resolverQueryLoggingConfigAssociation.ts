// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.
 */
export class ResolverQueryLoggingConfigAssociation extends pulumi.CustomResource {
    /**
     * Get an existing ResolverQueryLoggingConfigAssociation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ResolverQueryLoggingConfigAssociation {
        return new ResolverQueryLoggingConfigAssociation(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:route53resolver:ResolverQueryLoggingConfigAssociation';

    /**
     * Returns true if the given object is an instance of ResolverQueryLoggingConfigAssociation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ResolverQueryLoggingConfigAssociation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ResolverQueryLoggingConfigAssociation.__pulumiType;
    }

    /**
     * Rfc3339TimeString
     */
    public /*out*/ readonly creationTime!: pulumi.Output<string>;
    /**
     * ResolverQueryLogConfigAssociationError
     */
    public /*out*/ readonly error!: pulumi.Output<enums.route53resolver.ResolverQueryLoggingConfigAssociationError>;
    /**
     * ResolverQueryLogConfigAssociationErrorMessage
     */
    public /*out*/ readonly errorMessage!: pulumi.Output<string>;
    /**
     * ResolverQueryLogConfigId
     */
    public readonly resolverQueryLogConfigId!: pulumi.Output<string | undefined>;
    /**
     * ResourceId
     */
    public readonly resourceId!: pulumi.Output<string | undefined>;
    /**
     * ResolverQueryLogConfigAssociationStatus
     */
    public /*out*/ readonly status!: pulumi.Output<enums.route53resolver.ResolverQueryLoggingConfigAssociationStatus>;

    /**
     * Create a ResolverQueryLoggingConfigAssociation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ResolverQueryLoggingConfigAssociationArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            inputs["resolverQueryLogConfigId"] = args ? args.resolverQueryLogConfigId : undefined;
            inputs["resourceId"] = args ? args.resourceId : undefined;
            inputs["creationTime"] = undefined /*out*/;
            inputs["error"] = undefined /*out*/;
            inputs["errorMessage"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
        } else {
            inputs["creationTime"] = undefined /*out*/;
            inputs["error"] = undefined /*out*/;
            inputs["errorMessage"] = undefined /*out*/;
            inputs["resolverQueryLogConfigId"] = undefined /*out*/;
            inputs["resourceId"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ResolverQueryLoggingConfigAssociation.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ResolverQueryLoggingConfigAssociation resource.
 */
export interface ResolverQueryLoggingConfigAssociationArgs {
    /**
     * ResolverQueryLogConfigId
     */
    resolverQueryLogConfigId?: pulumi.Input<string>;
    /**
     * ResourceId
     */
    resourceId?: pulumi.Input<string>;
}
