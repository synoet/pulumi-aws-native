// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::DataBrew::Schedule.
 */
export class Schedule extends pulumi.CustomResource {
    /**
     * Get an existing Schedule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Schedule {
        return new Schedule(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:databrew:Schedule';

    /**
     * Returns true if the given object is an instance of Schedule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Schedule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Schedule.__pulumiType;
    }

    /**
     * Schedule cron
     */
    public readonly cronExpression!: pulumi.Output<string>;
    public readonly jobNames!: pulumi.Output<string[] | undefined>;
    /**
     * Schedule Name
     */
    public readonly name!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.databrew.ScheduleTag[] | undefined>;

    /**
     * Create a Schedule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ScheduleArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.cronExpression === undefined) && !opts.urn) {
                throw new Error("Missing required property 'cronExpression'");
            }
            resourceInputs["cronExpression"] = args ? args.cronExpression : undefined;
            resourceInputs["jobNames"] = args ? args.jobNames : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["cronExpression"] = undefined /*out*/;
            resourceInputs["jobNames"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Schedule.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Schedule resource.
 */
export interface ScheduleArgs {
    /**
     * Schedule cron
     */
    cronExpression: pulumi.Input<string>;
    jobNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Schedule Name
     */
    name?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.databrew.ScheduleTagArgs>[]>;
}
