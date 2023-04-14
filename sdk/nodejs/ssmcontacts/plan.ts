// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Engagement Plan for a SSM Incident Manager Contact.
 */
export class Plan extends pulumi.CustomResource {
    /**
     * Get an existing Plan resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Plan {
        return new Plan(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ssmcontacts:Plan';

    /**
     * Returns true if the given object is an instance of Plan.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Plan {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Plan.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the contact.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Contact ID for the AWS SSM Incident Manager Contact to associate the plan.
     */
    public readonly contactId!: pulumi.Output<string | undefined>;
    /**
     * Rotation Ids to associate with Oncall Contact for engagement.
     */
    public readonly rotationIds!: pulumi.Output<string[] | undefined>;
    /**
     * The stages that an escalation plan or engagement plan engages contacts and contact methods in.
     */
    public readonly stages!: pulumi.Output<outputs.ssmcontacts.PlanStage[] | undefined>;

    /**
     * Create a Plan resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: PlanArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["contactId"] = args ? args.contactId : undefined;
            resourceInputs["rotationIds"] = args ? args.rotationIds : undefined;
            resourceInputs["stages"] = args ? args.stages : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["contactId"] = undefined /*out*/;
            resourceInputs["rotationIds"] = undefined /*out*/;
            resourceInputs["stages"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Plan.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Plan resource.
 */
export interface PlanArgs {
    /**
     * Contact ID for the AWS SSM Incident Manager Contact to associate the plan.
     */
    contactId?: pulumi.Input<string>;
    /**
     * Rotation Ids to associate with Oncall Contact for engagement.
     */
    rotationIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The stages that an escalation plan or engagement plan engages contacts and contact methods in.
     */
    stages?: pulumi.Input<pulumi.Input<inputs.ssmcontacts.PlanStageArgs>[]>;
}
