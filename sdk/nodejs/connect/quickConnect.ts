// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Connect::QuickConnect
 */
export class QuickConnect extends pulumi.CustomResource {
    /**
     * Get an existing QuickConnect resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): QuickConnect {
        return new QuickConnect(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:connect:QuickConnect';

    /**
     * Returns true if the given object is an instance of QuickConnect.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is QuickConnect {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === QuickConnect.__pulumiType;
    }

    /**
     * The description of the quick connect.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The identifier of the Amazon Connect instance.
     */
    public readonly instanceArn!: pulumi.Output<string>;
    /**
     * The name of the quick connect.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) for the quick connect.
     */
    public /*out*/ readonly quickConnectArn!: pulumi.Output<string>;
    /**
     * Configuration settings for the quick connect.
     */
    public readonly quickConnectConfig!: pulumi.Output<outputs.connect.QuickConnectConfig>;
    /**
     * The type of quick connect. In the Amazon Connect console, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).
     */
    public /*out*/ readonly quickConnectType!: pulumi.Output<enums.connect.QuickConnectType>;
    /**
     * One or more tags.
     */
    public readonly tags!: pulumi.Output<outputs.connect.QuickConnectTag[] | undefined>;

    /**
     * Create a QuickConnect resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: QuickConnectArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.instanceArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceArn'");
            }
            if ((!args || args.quickConnectConfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'quickConnectConfig'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["instanceArn"] = args ? args.instanceArn : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["quickConnectConfig"] = args ? args.quickConnectConfig : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["quickConnectArn"] = undefined /*out*/;
            resourceInputs["quickConnectType"] = undefined /*out*/;
        } else {
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["instanceArn"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["quickConnectArn"] = undefined /*out*/;
            resourceInputs["quickConnectConfig"] = undefined /*out*/;
            resourceInputs["quickConnectType"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(QuickConnect.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a QuickConnect resource.
 */
export interface QuickConnectArgs {
    /**
     * The description of the quick connect.
     */
    description?: pulumi.Input<string>;
    /**
     * The identifier of the Amazon Connect instance.
     */
    instanceArn: pulumi.Input<string>;
    /**
     * The name of the quick connect.
     */
    name?: pulumi.Input<string>;
    /**
     * Configuration settings for the quick connect.
     */
    quickConnectConfig: pulumi.Input<inputs.connect.QuickConnectConfigArgs>;
    /**
     * One or more tags.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.connect.QuickConnectTagArgs>[]>;
}
