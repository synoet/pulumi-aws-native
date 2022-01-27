// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * RuleGroupsNamespace schema for cloudformation.
 */
export class RuleGroupsNamespace extends pulumi.CustomResource {
    /**
     * Get an existing RuleGroupsNamespace resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): RuleGroupsNamespace {
        return new RuleGroupsNamespace(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:aps:RuleGroupsNamespace';

    /**
     * Returns true if the given object is an instance of RuleGroupsNamespace.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RuleGroupsNamespace {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RuleGroupsNamespace.__pulumiType;
    }

    /**
     * The RuleGroupsNamespace ARN.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The RuleGroupsNamespace data.
     */
    public readonly data!: pulumi.Output<string>;
    /**
     * The RuleGroupsNamespace name.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.aps.RuleGroupsNamespaceTag[] | undefined>;
    /**
     * Required to identify a specific APS Workspace associated with this RuleGroupsNamespace.
     */
    public readonly workspace!: pulumi.Output<string>;

    /**
     * Create a RuleGroupsNamespace resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RuleGroupsNamespaceArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.data === undefined) && !opts.urn) {
                throw new Error("Missing required property 'data'");
            }
            if ((!args || args.workspace === undefined) && !opts.urn) {
                throw new Error("Missing required property 'workspace'");
            }
            resourceInputs["data"] = args ? args.data : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["workspace"] = args ? args.workspace : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["data"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["workspace"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(RuleGroupsNamespace.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a RuleGroupsNamespace resource.
 */
export interface RuleGroupsNamespaceArgs {
    /**
     * The RuleGroupsNamespace data.
     */
    data: pulumi.Input<string>;
    /**
     * The RuleGroupsNamespace name.
     */
    name?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.aps.RuleGroupsNamespaceTagArgs>[]>;
    /**
     * Required to identify a specific APS Workspace associated with this RuleGroupsNamespace.
     */
    workspace: pulumi.Input<string>;
}
