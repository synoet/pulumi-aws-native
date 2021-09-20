// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::Athena::WorkGroup
 */
export class WorkGroup extends pulumi.CustomResource {
    /**
     * Get an existing WorkGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): WorkGroup {
        return new WorkGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:athena:WorkGroup';

    /**
     * Returns true if the given object is an instance of WorkGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is WorkGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === WorkGroup.__pulumiType;
    }

    /**
     * The date and time the workgroup was created.
     */
    public /*out*/ readonly creationTime!: pulumi.Output<string>;
    /**
     * The workgroup description.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The workGroup name.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The option to delete the workgroup and its contents even if the workgroup contains any named queries.
     */
    public readonly recursiveDeleteOption!: pulumi.Output<boolean | undefined>;
    /**
     * The state of the workgroup: ENABLED or DISABLED.
     */
    public readonly state!: pulumi.Output<enums.athena.WorkGroupState | undefined>;
    /**
     * One or more tags, separated by commas, that you want to attach to the workgroup as you create it
     */
    public readonly tags!: pulumi.Output<outputs.athena.WorkGroupTag[] | undefined>;
    /**
     * The workgroup configuration
     */
    public readonly workGroupConfiguration!: pulumi.Output<outputs.athena.WorkGroupWorkGroupConfiguration | undefined>;
    /**
     * The workgroup configuration update object
     */
    public readonly workGroupConfigurationUpdates!: pulumi.Output<outputs.athena.WorkGroupWorkGroupConfigurationUpdates | undefined>;

    /**
     * Create a WorkGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WorkGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["recursiveDeleteOption"] = args ? args.recursiveDeleteOption : undefined;
            inputs["state"] = args ? args.state : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["workGroupConfiguration"] = args ? args.workGroupConfiguration : undefined;
            inputs["workGroupConfigurationUpdates"] = args ? args.workGroupConfigurationUpdates : undefined;
            inputs["creationTime"] = undefined /*out*/;
        } else {
            inputs["creationTime"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["recursiveDeleteOption"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["workGroupConfiguration"] = undefined /*out*/;
            inputs["workGroupConfigurationUpdates"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(WorkGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a WorkGroup resource.
 */
export interface WorkGroupArgs {
    /**
     * The workgroup description.
     */
    description?: pulumi.Input<string>;
    /**
     * The workGroup name.
     */
    name: pulumi.Input<string>;
    /**
     * The option to delete the workgroup and its contents even if the workgroup contains any named queries.
     */
    recursiveDeleteOption?: pulumi.Input<boolean>;
    /**
     * The state of the workgroup: ENABLED or DISABLED.
     */
    state?: pulumi.Input<enums.athena.WorkGroupState>;
    /**
     * One or more tags, separated by commas, that you want to attach to the workgroup as you create it
     */
    tags?: pulumi.Input<pulumi.Input<inputs.athena.WorkGroupTagArgs>[]>;
    /**
     * The workgroup configuration
     */
    workGroupConfiguration?: pulumi.Input<inputs.athena.WorkGroupWorkGroupConfigurationArgs>;
    /**
     * The workgroup configuration update object
     */
    workGroupConfigurationUpdates?: pulumi.Input<inputs.athena.WorkGroupWorkGroupConfigurationUpdatesArgs>;
}
