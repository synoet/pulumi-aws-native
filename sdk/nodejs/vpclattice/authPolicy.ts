// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Creates or updates the auth policy.
 */
export class AuthPolicy extends pulumi.CustomResource {
    /**
     * Get an existing AuthPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AuthPolicy {
        return new AuthPolicy(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:vpclattice:AuthPolicy';

    /**
     * Returns true if the given object is an instance of AuthPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AuthPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AuthPolicy.__pulumiType;
    }

    public readonly policy!: pulumi.Output<any>;
    public readonly resourceIdentifier!: pulumi.Output<string>;
    public /*out*/ readonly state!: pulumi.Output<enums.vpclattice.AuthPolicyState>;

    /**
     * Create a AuthPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AuthPolicyArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.policy === undefined) && !opts.urn) {
                throw new Error("Missing required property 'policy'");
            }
            if ((!args || args.resourceIdentifier === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceIdentifier'");
            }
            resourceInputs["policy"] = args ? args.policy : undefined;
            resourceInputs["resourceIdentifier"] = args ? args.resourceIdentifier : undefined;
            resourceInputs["state"] = undefined /*out*/;
        } else {
            resourceInputs["policy"] = undefined /*out*/;
            resourceInputs["resourceIdentifier"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["resourceIdentifier"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(AuthPolicy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a AuthPolicy resource.
 */
export interface AuthPolicyArgs {
    policy: any;
    resourceIdentifier: pulumi.Input<string>;
}
