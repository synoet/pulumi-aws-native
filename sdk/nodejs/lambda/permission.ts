// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Lambda::Permission
 *
 * @deprecated Permission is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Permission extends pulumi.CustomResource {
    /**
     * Get an existing Permission resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Permission {
        pulumi.log.warn("Permission is deprecated: Permission is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Permission(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:lambda:Permission';

    /**
     * Returns true if the given object is an instance of Permission.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Permission {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Permission.__pulumiType;
    }

    public readonly action!: pulumi.Output<string>;
    public readonly eventSourceToken!: pulumi.Output<string | undefined>;
    public readonly functionName!: pulumi.Output<string>;
    public readonly principal!: pulumi.Output<string>;
    public readonly sourceAccount!: pulumi.Output<string | undefined>;
    public readonly sourceArn!: pulumi.Output<string | undefined>;

    /**
     * Create a Permission resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Permission is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: PermissionArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Permission is deprecated: Permission is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.action === undefined) && !opts.urn) {
                throw new Error("Missing required property 'action'");
            }
            if ((!args || args.functionName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'functionName'");
            }
            if ((!args || args.principal === undefined) && !opts.urn) {
                throw new Error("Missing required property 'principal'");
            }
            resourceInputs["action"] = args ? args.action : undefined;
            resourceInputs["eventSourceToken"] = args ? args.eventSourceToken : undefined;
            resourceInputs["functionName"] = args ? args.functionName : undefined;
            resourceInputs["principal"] = args ? args.principal : undefined;
            resourceInputs["sourceAccount"] = args ? args.sourceAccount : undefined;
            resourceInputs["sourceArn"] = args ? args.sourceArn : undefined;
        } else {
            resourceInputs["action"] = undefined /*out*/;
            resourceInputs["eventSourceToken"] = undefined /*out*/;
            resourceInputs["functionName"] = undefined /*out*/;
            resourceInputs["principal"] = undefined /*out*/;
            resourceInputs["sourceAccount"] = undefined /*out*/;
            resourceInputs["sourceArn"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Permission.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Permission resource.
 */
export interface PermissionArgs {
    action: pulumi.Input<string>;
    eventSourceToken?: pulumi.Input<string>;
    functionName: pulumi.Input<string>;
    principal: pulumi.Input<string>;
    sourceAccount?: pulumi.Input<string>;
    sourceArn?: pulumi.Input<string>;
}
