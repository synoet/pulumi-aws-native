// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Connect::TaskTemplate.
 */
export class TaskTemplate extends pulumi.CustomResource {
    /**
     * Get an existing TaskTemplate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): TaskTemplate {
        return new TaskTemplate(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:connect:TaskTemplate';

    /**
     * Returns true if the given object is an instance of TaskTemplate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TaskTemplate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TaskTemplate.__pulumiType;
    }

    /**
     * The identifier (arn) of the task template.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly clientToken!: pulumi.Output<string | undefined>;
    /**
     * The constraints for the task template
     */
    public readonly constraints!: pulumi.Output<outputs.connect.ConstraintsProperties | undefined>;
    /**
     * The identifier of the contact flow.
     */
    public readonly contactFlowArn!: pulumi.Output<string | undefined>;
    public readonly defaults!: pulumi.Output<outputs.connect.TaskTemplateDefaultFieldValue[] | undefined>;
    /**
     * The description of the task template.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The list of task template's fields
     */
    public readonly fields!: pulumi.Output<outputs.connect.TaskTemplateField[] | undefined>;
    /**
     * The identifier (arn) of the instance.
     */
    public readonly instanceArn!: pulumi.Output<string>;
    /**
     * The name of the task template.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    public readonly status!: pulumi.Output<enums.connect.TaskTemplateStatus | undefined>;
    /**
     * One or more tags.
     */
    public readonly tags!: pulumi.Output<outputs.connect.TaskTemplateTag[] | undefined>;

    /**
     * Create a TaskTemplate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TaskTemplateArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.instanceArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceArn'");
            }
            resourceInputs["clientToken"] = args ? args.clientToken : undefined;
            resourceInputs["constraints"] = args ? args.constraints : undefined;
            resourceInputs["contactFlowArn"] = args ? args.contactFlowArn : undefined;
            resourceInputs["defaults"] = args ? args.defaults : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["fields"] = args ? args.fields : undefined;
            resourceInputs["instanceArn"] = args ? args.instanceArn : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["status"] = args ? args.status : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["clientToken"] = undefined /*out*/;
            resourceInputs["constraints"] = undefined /*out*/;
            resourceInputs["contactFlowArn"] = undefined /*out*/;
            resourceInputs["defaults"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["fields"] = undefined /*out*/;
            resourceInputs["instanceArn"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(TaskTemplate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a TaskTemplate resource.
 */
export interface TaskTemplateArgs {
    clientToken?: pulumi.Input<string>;
    /**
     * The constraints for the task template
     */
    constraints?: pulumi.Input<inputs.connect.ConstraintsPropertiesArgs>;
    /**
     * The identifier of the contact flow.
     */
    contactFlowArn?: pulumi.Input<string>;
    defaults?: pulumi.Input<pulumi.Input<inputs.connect.TaskTemplateDefaultFieldValueArgs>[]>;
    /**
     * The description of the task template.
     */
    description?: pulumi.Input<string>;
    /**
     * The list of task template's fields
     */
    fields?: pulumi.Input<pulumi.Input<inputs.connect.TaskTemplateFieldArgs>[]>;
    /**
     * The identifier (arn) of the instance.
     */
    instanceArn: pulumi.Input<string>;
    /**
     * The name of the task template.
     */
    name?: pulumi.Input<string>;
    status?: pulumi.Input<enums.connect.TaskTemplateStatus>;
    /**
     * One or more tags.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.connect.TaskTemplateTagArgs>[]>;
}
