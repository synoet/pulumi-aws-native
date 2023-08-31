// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElastiCache::UserGroup
 */
export class UserGroup extends pulumi.CustomResource {
    /**
     * Get an existing UserGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): UserGroup {
        return new UserGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:elasticache:UserGroup';

    /**
     * Returns true if the given object is an instance of UserGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is UserGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === UserGroup.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the user account.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Must be redis.
     */
    public readonly engine!: pulumi.Output<enums.elasticache.UserGroupEngine>;
    /**
     * Indicates user group status. Can be "creating", "active", "modifying", "deleting".
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this user.
     */
    public readonly tags!: pulumi.Output<outputs.elasticache.UserGroupTag[] | undefined>;
    /**
     * The ID of the user group.
     */
    public readonly userGroupId!: pulumi.Output<string>;
    /**
     * List of users associated to this user group.
     */
    public readonly userIds!: pulumi.Output<string[]>;

    /**
     * Create a UserGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.engine === undefined) && !opts.urn) {
                throw new Error("Missing required property 'engine'");
            }
            if ((!args || args.userGroupId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'userGroupId'");
            }
            if ((!args || args.userIds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'userIds'");
            }
            resourceInputs["engine"] = args ? args.engine : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["userGroupId"] = args ? args.userGroupId : undefined;
            resourceInputs["userIds"] = args ? args.userIds : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["engine"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["userGroupId"] = undefined /*out*/;
            resourceInputs["userIds"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["engine", "userGroupId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(UserGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a UserGroup resource.
 */
export interface UserGroupArgs {
    /**
     * Must be redis.
     */
    engine: pulumi.Input<enums.elasticache.UserGroupEngine>;
    /**
     * An array of key-value pairs to apply to this user.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.elasticache.UserGroupTagArgs>[]>;
    /**
     * The ID of the user group.
     */
    userGroupId: pulumi.Input<string>;
    /**
     * List of users associated to this user group.
     */
    userIds: pulumi.Input<pulumi.Input<string>[]>;
}
