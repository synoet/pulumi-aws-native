// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Amazon OpenSearchServerless security policy resource
 */
export class SecurityPolicy extends pulumi.CustomResource {
    /**
     * Get an existing SecurityPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SecurityPolicy {
        return new SecurityPolicy(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:opensearchserverless:SecurityPolicy';

    /**
     * Returns true if the given object is an instance of SecurityPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SecurityPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SecurityPolicy.__pulumiType;
    }

    /**
     * The description of the policy
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name of the policy
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The JSON policy document that is the content for the policy
     */
    public readonly policy!: pulumi.Output<string>;
    public readonly type!: pulumi.Output<enums.opensearchserverless.SecurityPolicyType>;

    /**
     * Create a SecurityPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SecurityPolicyArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.policy === undefined) && !opts.urn) {
                throw new Error("Missing required property 'policy'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["policy"] = args ? args.policy : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
        } else {
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["policy"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name", "type"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(SecurityPolicy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a SecurityPolicy resource.
 */
export interface SecurityPolicyArgs {
    /**
     * The description of the policy
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the policy
     */
    name?: pulumi.Input<string>;
    /**
     * The JSON policy document that is the content for the policy
     */
    policy: pulumi.Input<string>;
    type: pulumi.Input<enums.opensearchserverless.SecurityPolicyType>;
}
