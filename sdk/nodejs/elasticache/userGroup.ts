// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html
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

    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-engine
     */
    public readonly engine!: pulumi.Output<string>;
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-usergroupid
     */
    public readonly userGroupId!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-userids
     */
    public readonly userIds!: pulumi.Output<string[] | undefined>;

    /**
     * Create a UserGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.engine === undefined) && !opts.urn) {
                throw new Error("Missing required property 'engine'");
            }
            if ((!args || args.userGroupId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'userGroupId'");
            }
            inputs["engine"] = args ? args.engine : undefined;
            inputs["userGroupId"] = args ? args.userGroupId : undefined;
            inputs["userIds"] = args ? args.userIds : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["engine"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
            inputs["userGroupId"] = undefined /*out*/;
            inputs["userIds"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(UserGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a UserGroup resource.
 */
export interface UserGroupArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-engine
     */
    engine: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-usergroupid
     */
    userGroupId: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-userids
     */
    userIds?: pulumi.Input<pulumi.Input<string>[]>;
}
