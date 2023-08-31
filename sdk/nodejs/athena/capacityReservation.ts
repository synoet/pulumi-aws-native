// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::Athena::CapacityReservation
 */
export class CapacityReservation extends pulumi.CustomResource {
    /**
     * Get an existing CapacityReservation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): CapacityReservation {
        return new CapacityReservation(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:athena:CapacityReservation';

    /**
     * Returns true if the given object is an instance of CapacityReservation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CapacityReservation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CapacityReservation.__pulumiType;
    }

    /**
     * The number of DPUs Athena has provisioned and allocated for the reservation
     */
    public /*out*/ readonly allocatedDpus!: pulumi.Output<number>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly capacityAssignmentConfiguration!: pulumi.Output<outputs.athena.CapacityReservationCapacityAssignmentConfiguration | undefined>;
    /**
     * The date and time the reservation was created.
     */
    public /*out*/ readonly creationTime!: pulumi.Output<string>;
    /**
     * The timestamp when the last successful allocated was made
     */
    public /*out*/ readonly lastSuccessfulAllocationTime!: pulumi.Output<string>;
    /**
     * The reservation name.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The status of the reservation.
     */
    public /*out*/ readonly status!: pulumi.Output<enums.athena.CapacityReservationStatus>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.athena.CapacityReservationTag[] | undefined>;
    /**
     * The number of DPUs to request to be allocated to the reservation.
     */
    public readonly targetDpus!: pulumi.Output<number>;

    /**
     * Create a CapacityReservation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CapacityReservationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.targetDpus === undefined) && !opts.urn) {
                throw new Error("Missing required property 'targetDpus'");
            }
            resourceInputs["capacityAssignmentConfiguration"] = args ? args.capacityAssignmentConfiguration : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["targetDpus"] = args ? args.targetDpus : undefined;
            resourceInputs["allocatedDpus"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["lastSuccessfulAllocationTime"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        } else {
            resourceInputs["allocatedDpus"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["capacityAssignmentConfiguration"] = undefined /*out*/;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["lastSuccessfulAllocationTime"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["targetDpus"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(CapacityReservation.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a CapacityReservation resource.
 */
export interface CapacityReservationArgs {
    capacityAssignmentConfiguration?: pulumi.Input<inputs.athena.CapacityReservationCapacityAssignmentConfigurationArgs>;
    /**
     * The reservation name.
     */
    name?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.athena.CapacityReservationTagArgs>[]>;
    /**
     * The number of DPUs to request to be allocated to the reservation.
     */
    targetDpus: pulumi.Input<number>;
}
