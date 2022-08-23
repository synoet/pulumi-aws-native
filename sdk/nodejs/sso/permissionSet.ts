// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for SSO PermissionSet
 */
export class PermissionSet extends pulumi.CustomResource {
    /**
     * Get an existing PermissionSet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): PermissionSet {
        return new PermissionSet(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:sso:PermissionSet';

    /**
     * Returns true if the given object is an instance of PermissionSet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PermissionSet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PermissionSet.__pulumiType;
    }

    public readonly customerManagedPolicyReferences!: pulumi.Output<outputs.sso.PermissionSetCustomerManagedPolicyReference[] | undefined>;
    /**
     * The permission set description.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The inline policy to put in permission set.
     */
    public readonly inlinePolicy!: pulumi.Output<any | undefined>;
    /**
     * The sso instance arn that the permission set is owned.
     */
    public readonly instanceArn!: pulumi.Output<string>;
    public readonly managedPolicies!: pulumi.Output<string[] | undefined>;
    /**
     * The name you want to assign to this permission set.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The permission set that the policy will be attached to
     */
    public /*out*/ readonly permissionSetArn!: pulumi.Output<string>;
    public readonly permissionsBoundary!: pulumi.Output<outputs.sso.PermissionSetPermissionsBoundary | undefined>;
    /**
     * The relay state URL that redirect links to any service in the AWS Management Console.
     */
    public readonly relayStateType!: pulumi.Output<string | undefined>;
    /**
     * The length of time that a user can be signed in to an AWS account.
     */
    public readonly sessionDuration!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.sso.PermissionSetTag[] | undefined>;

    /**
     * Create a PermissionSet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PermissionSetArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.instanceArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceArn'");
            }
            resourceInputs["customerManagedPolicyReferences"] = args ? args.customerManagedPolicyReferences : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["inlinePolicy"] = args ? args.inlinePolicy : undefined;
            resourceInputs["instanceArn"] = args ? args.instanceArn : undefined;
            resourceInputs["managedPolicies"] = args ? args.managedPolicies : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["permissionsBoundary"] = args ? args.permissionsBoundary : undefined;
            resourceInputs["relayStateType"] = args ? args.relayStateType : undefined;
            resourceInputs["sessionDuration"] = args ? args.sessionDuration : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["permissionSetArn"] = undefined /*out*/;
        } else {
            resourceInputs["customerManagedPolicyReferences"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["inlinePolicy"] = undefined /*out*/;
            resourceInputs["instanceArn"] = undefined /*out*/;
            resourceInputs["managedPolicies"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["permissionSetArn"] = undefined /*out*/;
            resourceInputs["permissionsBoundary"] = undefined /*out*/;
            resourceInputs["relayStateType"] = undefined /*out*/;
            resourceInputs["sessionDuration"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(PermissionSet.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a PermissionSet resource.
 */
export interface PermissionSetArgs {
    customerManagedPolicyReferences?: pulumi.Input<pulumi.Input<inputs.sso.PermissionSetCustomerManagedPolicyReferenceArgs>[]>;
    /**
     * The permission set description.
     */
    description?: pulumi.Input<string>;
    /**
     * The inline policy to put in permission set.
     */
    inlinePolicy?: any;
    /**
     * The sso instance arn that the permission set is owned.
     */
    instanceArn: pulumi.Input<string>;
    managedPolicies?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name you want to assign to this permission set.
     */
    name?: pulumi.Input<string>;
    permissionsBoundary?: pulumi.Input<inputs.sso.PermissionSetPermissionsBoundaryArgs>;
    /**
     * The relay state URL that redirect links to any service in the AWS Management Console.
     */
    relayStateType?: pulumi.Input<string>;
    /**
     * The length of time that a user can be signed in to an AWS account.
     */
    sessionDuration?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.sso.PermissionSetTagArgs>[]>;
}
