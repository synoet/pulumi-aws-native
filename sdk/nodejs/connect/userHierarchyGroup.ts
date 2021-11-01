// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Connect::UserHierarchyGroup
 */
export class UserHierarchyGroup extends pulumi.CustomResource {
    /**
     * Get an existing UserHierarchyGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): UserHierarchyGroup {
        return new UserHierarchyGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:connect:UserHierarchyGroup';

    /**
     * Returns true if the given object is an instance of UserHierarchyGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is UserHierarchyGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === UserHierarchyGroup.__pulumiType;
    }

    /**
     * The identifier of the Amazon Connect instance.
     */
    public readonly instanceArn!: pulumi.Output<string>;
    /**
     * The name of the user hierarchy group.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) for the parent user hierarchy group.
     */
    public readonly parentGroupArn!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) for the user hierarchy group.
     */
    public /*out*/ readonly userHierarchyGroupArn!: pulumi.Output<string>;

    /**
     * Create a UserHierarchyGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserHierarchyGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.instanceArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceArn'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            inputs["instanceArn"] = args ? args.instanceArn : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["parentGroupArn"] = args ? args.parentGroupArn : undefined;
            inputs["userHierarchyGroupArn"] = undefined /*out*/;
        } else {
            inputs["instanceArn"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["parentGroupArn"] = undefined /*out*/;
            inputs["userHierarchyGroupArn"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(UserHierarchyGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a UserHierarchyGroup resource.
 */
export interface UserHierarchyGroupArgs {
    /**
     * The identifier of the Amazon Connect instance.
     */
    instanceArn: pulumi.Input<string>;
    /**
     * The name of the user hierarchy group.
     */
    name: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) for the parent user hierarchy group.
     */
    parentGroupArn?: pulumi.Input<string>;
}
