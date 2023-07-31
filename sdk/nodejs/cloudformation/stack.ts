// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CloudFormation::Stack
 *
 * @deprecated Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Stack extends pulumi.CustomResource {
    /**
     * Get an existing Stack resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Stack {
        pulumi.log.warn("Stack is deprecated: Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Stack(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cloudformation:Stack';

    /**
     * Returns true if the given object is an instance of Stack.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Stack {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Stack.__pulumiType;
    }

    public readonly notificationArns!: pulumi.Output<string[] | undefined>;
    public readonly parameters!: pulumi.Output<any | undefined>;
    public readonly tags!: pulumi.Output<outputs.cloudformation.StackTag[] | undefined>;
    public readonly templateUrl!: pulumi.Output<string>;
    public readonly timeoutInMinutes!: pulumi.Output<number | undefined>;

    /**
     * Create a Stack resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: StackArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Stack is deprecated: Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.templateUrl === undefined) && !opts.urn) {
                throw new Error("Missing required property 'templateUrl'");
            }
            resourceInputs["notificationArns"] = args ? args.notificationArns : undefined;
            resourceInputs["parameters"] = args ? args.parameters : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["templateUrl"] = args ? args.templateUrl : undefined;
            resourceInputs["timeoutInMinutes"] = args ? args.timeoutInMinutes : undefined;
        } else {
            resourceInputs["notificationArns"] = undefined /*out*/;
            resourceInputs["parameters"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["templateUrl"] = undefined /*out*/;
            resourceInputs["timeoutInMinutes"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Stack.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Stack resource.
 */
export interface StackArgs {
    notificationArns?: pulumi.Input<pulumi.Input<string>[]>;
    parameters?: any;
    tags?: pulumi.Input<pulumi.Input<inputs.cloudformation.StackTagArgs>[]>;
    templateUrl: pulumi.Input<string>;
    timeoutInMinutes?: pulumi.Input<number>;
}
