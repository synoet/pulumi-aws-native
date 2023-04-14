// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::GameCast::StreamGroup Resource Type
 */
export class StreamGroup extends pulumi.CustomResource {
    /**
     * Get an existing StreamGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): StreamGroup {
        return new StreamGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:gamecast:StreamGroup';

    /**
     * Returns true if the given object is an instance of StreamGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is StreamGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === StreamGroup.__pulumiType;
    }

    /**
     * ARN of the resource.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly defaultApplication!: pulumi.Output<outputs.gamecast.StreamGroupDefaultApplication | undefined>;
    /**
     * Descriptive label for the resource, not a unique ID.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * DesiredCapacity is the target number of stream sessions customer sets.
     */
    public readonly desiredCapacity!: pulumi.Output<number | undefined>;
    public readonly streamClass!: pulumi.Output<enums.gamecast.StreamGroupStreamClass | undefined>;
    public readonly tags!: pulumi.Output<outputs.gamecast.StreamGroupTags | undefined>;

    /**
     * Create a StreamGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StreamGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            resourceInputs["defaultApplication"] = args ? args.defaultApplication : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["desiredCapacity"] = args ? args.desiredCapacity : undefined;
            resourceInputs["streamClass"] = args ? args.streamClass : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["defaultApplication"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["desiredCapacity"] = undefined /*out*/;
            resourceInputs["streamClass"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(StreamGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a StreamGroup resource.
 */
export interface StreamGroupArgs {
    defaultApplication?: pulumi.Input<inputs.gamecast.StreamGroupDefaultApplicationArgs>;
    /**
     * Descriptive label for the resource, not a unique ID.
     */
    description: pulumi.Input<string>;
    /**
     * DesiredCapacity is the target number of stream sessions customer sets.
     */
    desiredCapacity?: pulumi.Input<number>;
    streamClass?: pulumi.Input<enums.gamecast.StreamGroupStreamClass>;
    tags?: pulumi.Input<inputs.gamecast.StreamGroupTagsArgs>;
}
