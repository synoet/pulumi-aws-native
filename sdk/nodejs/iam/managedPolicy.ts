// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IAM::ManagedPolicy
 */
export class ManagedPolicy extends pulumi.CustomResource {
    /**
     * Get an existing ManagedPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ManagedPolicy {
        return new ManagedPolicy(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iam:ManagedPolicy';

    /**
     * Returns true if the given object is an instance of ManagedPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ManagedPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ManagedPolicy.__pulumiType;
    }

    /**
     * The number of entities (users, groups, and roles) that the policy is attached to.
     */
    public /*out*/ readonly attachmentCount!: pulumi.Output<number>;
    /**
     * The date and time, in ISO 8601 date-time format, when the policy was created.
     */
    public /*out*/ readonly createDate!: pulumi.Output<string>;
    /**
     * The identifier for the version of the policy that is set as the default version.
     */
    public /*out*/ readonly defaultVersionId!: pulumi.Output<string>;
    /**
     * A friendly description of the policy.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name (friendly name, not ARN) of the group to attach the policy to.
     */
    public readonly groups!: pulumi.Output<string[] | undefined>;
    /**
     * Specifies whether the policy can be attached to an IAM user, group, or role.
     */
    public /*out*/ readonly isAttachable!: pulumi.Output<boolean>;
    /**
     * The friendly name of the policy.
     */
    public readonly managedPolicyName!: pulumi.Output<string | undefined>;
    /**
     * The path for the policy.
     */
    public readonly path!: pulumi.Output<string | undefined>;
    /**
     * The number of entities (users and roles) for which the policy is used to set the permissions boundary.
     */
    public /*out*/ readonly permissionsBoundaryUsageCount!: pulumi.Output<number>;
    /**
     * Amazon Resource Name (ARN) of the managed policy
     */
    public /*out*/ readonly policyArn!: pulumi.Output<string>;
    /**
     * The JSON policy document that you want to use as the content for the new policy.
     */
    public readonly policyDocument!: pulumi.Output<any>;
    /**
     * The stable and unique string identifying the policy.
     */
    public /*out*/ readonly policyId!: pulumi.Output<string>;
    /**
     * The name (friendly name, not ARN) of the role to attach the policy to.
     */
    public readonly roles!: pulumi.Output<string[] | undefined>;
    /**
     * The date and time, in ISO 8601 date-time format, when the policy was last updated.
     */
    public /*out*/ readonly updateDate!: pulumi.Output<string>;
    /**
     * The name (friendly name, not ARN) of the IAM user to attach the policy to.
     */
    public readonly users!: pulumi.Output<string[] | undefined>;

    /**
     * Create a ManagedPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ManagedPolicyArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.policyDocument === undefined) && !opts.urn) {
                throw new Error("Missing required property 'policyDocument'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["groups"] = args ? args.groups : undefined;
            resourceInputs["managedPolicyName"] = args ? args.managedPolicyName : undefined;
            resourceInputs["path"] = args ? args.path : undefined;
            resourceInputs["policyDocument"] = args ? args.policyDocument : undefined;
            resourceInputs["roles"] = args ? args.roles : undefined;
            resourceInputs["users"] = args ? args.users : undefined;
            resourceInputs["attachmentCount"] = undefined /*out*/;
            resourceInputs["createDate"] = undefined /*out*/;
            resourceInputs["defaultVersionId"] = undefined /*out*/;
            resourceInputs["isAttachable"] = undefined /*out*/;
            resourceInputs["permissionsBoundaryUsageCount"] = undefined /*out*/;
            resourceInputs["policyArn"] = undefined /*out*/;
            resourceInputs["policyId"] = undefined /*out*/;
            resourceInputs["updateDate"] = undefined /*out*/;
        } else {
            resourceInputs["attachmentCount"] = undefined /*out*/;
            resourceInputs["createDate"] = undefined /*out*/;
            resourceInputs["defaultVersionId"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["groups"] = undefined /*out*/;
            resourceInputs["isAttachable"] = undefined /*out*/;
            resourceInputs["managedPolicyName"] = undefined /*out*/;
            resourceInputs["path"] = undefined /*out*/;
            resourceInputs["permissionsBoundaryUsageCount"] = undefined /*out*/;
            resourceInputs["policyArn"] = undefined /*out*/;
            resourceInputs["policyDocument"] = undefined /*out*/;
            resourceInputs["policyId"] = undefined /*out*/;
            resourceInputs["roles"] = undefined /*out*/;
            resourceInputs["updateDate"] = undefined /*out*/;
            resourceInputs["users"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["description", "managedPolicyName", "path"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ManagedPolicy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ManagedPolicy resource.
 */
export interface ManagedPolicyArgs {
    /**
     * A friendly description of the policy.
     */
    description?: pulumi.Input<string>;
    /**
     * The name (friendly name, not ARN) of the group to attach the policy to.
     */
    groups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The friendly name of the policy.
     */
    managedPolicyName?: pulumi.Input<string>;
    /**
     * The path for the policy.
     */
    path?: pulumi.Input<string>;
    /**
     * The JSON policy document that you want to use as the content for the new policy.
     */
    policyDocument: any;
    /**
     * The name (friendly name, not ARN) of the role to attach the policy to.
     */
    roles?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name (friendly name, not ARN) of the IAM user to attach the policy to.
     */
    users?: pulumi.Input<pulumi.Input<string>[]>;
}
