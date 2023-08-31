// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Creates a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions.
 */
export class Rule extends pulumi.CustomResource {
    /**
     * Get an existing Rule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Rule {
        return new Rule(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:vpclattice:Rule';

    /**
     * Returns true if the given object is an instance of Rule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Rule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Rule.__pulumiType;
    }

    public readonly action!: pulumi.Output<outputs.vpclattice.RuleAction>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly listenerIdentifier!: pulumi.Output<string | undefined>;
    public readonly match!: pulumi.Output<outputs.vpclattice.RuleMatch>;
    public readonly name!: pulumi.Output<string | undefined>;
    public readonly priority!: pulumi.Output<number>;
    public readonly serviceIdentifier!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.vpclattice.RuleTag[] | undefined>;

    /**
     * Create a Rule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RuleArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.action === undefined) && !opts.urn) {
                throw new Error("Missing required property 'action'");
            }
            if ((!args || args.match === undefined) && !opts.urn) {
                throw new Error("Missing required property 'match'");
            }
            if ((!args || args.priority === undefined) && !opts.urn) {
                throw new Error("Missing required property 'priority'");
            }
            resourceInputs["action"] = args ? args.action : undefined;
            resourceInputs["listenerIdentifier"] = args ? args.listenerIdentifier : undefined;
            resourceInputs["match"] = args ? args.match : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["priority"] = args ? args.priority : undefined;
            resourceInputs["serviceIdentifier"] = args ? args.serviceIdentifier : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["action"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["listenerIdentifier"] = undefined /*out*/;
            resourceInputs["match"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["priority"] = undefined /*out*/;
            resourceInputs["serviceIdentifier"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["listenerIdentifier", "name", "serviceIdentifier"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Rule.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Rule resource.
 */
export interface RuleArgs {
    action: pulumi.Input<inputs.vpclattice.RuleActionArgs>;
    listenerIdentifier?: pulumi.Input<string>;
    match: pulumi.Input<inputs.vpclattice.RuleMatchArgs>;
    name?: pulumi.Input<string>;
    priority: pulumi.Input<number>;
    serviceIdentifier?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.vpclattice.RuleTagArgs>[]>;
}
