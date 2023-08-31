// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::CapacityReservation
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
    public static readonly __pulumiType = 'aws-native:ec2:CapacityReservation';

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

    public readonly availabilityZone!: pulumi.Output<string>;
    public /*out*/ readonly availableInstanceCount!: pulumi.Output<number>;
    public readonly ebsOptimized!: pulumi.Output<boolean | undefined>;
    public readonly endDate!: pulumi.Output<string | undefined>;
    public readonly endDateType!: pulumi.Output<string | undefined>;
    public readonly ephemeralStorage!: pulumi.Output<boolean | undefined>;
    public readonly instanceCount!: pulumi.Output<number>;
    public readonly instanceMatchCriteria!: pulumi.Output<string | undefined>;
    public readonly instancePlatform!: pulumi.Output<string>;
    public readonly instanceType!: pulumi.Output<string>;
    public readonly outPostArn!: pulumi.Output<string | undefined>;
    public readonly placementGroupArn!: pulumi.Output<string | undefined>;
    public readonly tagSpecifications!: pulumi.Output<outputs.ec2.CapacityReservationTagSpecification[] | undefined>;
    public readonly tenancy!: pulumi.Output<string | undefined>;
    public /*out*/ readonly totalInstanceCount!: pulumi.Output<number>;

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
            if ((!args || args.availabilityZone === undefined) && !opts.urn) {
                throw new Error("Missing required property 'availabilityZone'");
            }
            if ((!args || args.instanceCount === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceCount'");
            }
            if ((!args || args.instancePlatform === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instancePlatform'");
            }
            if ((!args || args.instanceType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceType'");
            }
            resourceInputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            resourceInputs["ebsOptimized"] = args ? args.ebsOptimized : undefined;
            resourceInputs["endDate"] = args ? args.endDate : undefined;
            resourceInputs["endDateType"] = args ? args.endDateType : undefined;
            resourceInputs["ephemeralStorage"] = args ? args.ephemeralStorage : undefined;
            resourceInputs["instanceCount"] = args ? args.instanceCount : undefined;
            resourceInputs["instanceMatchCriteria"] = args ? args.instanceMatchCriteria : undefined;
            resourceInputs["instancePlatform"] = args ? args.instancePlatform : undefined;
            resourceInputs["instanceType"] = args ? args.instanceType : undefined;
            resourceInputs["outPostArn"] = args ? args.outPostArn : undefined;
            resourceInputs["placementGroupArn"] = args ? args.placementGroupArn : undefined;
            resourceInputs["tagSpecifications"] = args ? args.tagSpecifications : undefined;
            resourceInputs["tenancy"] = args ? args.tenancy : undefined;
            resourceInputs["availableInstanceCount"] = undefined /*out*/;
            resourceInputs["totalInstanceCount"] = undefined /*out*/;
        } else {
            resourceInputs["availabilityZone"] = undefined /*out*/;
            resourceInputs["availableInstanceCount"] = undefined /*out*/;
            resourceInputs["ebsOptimized"] = undefined /*out*/;
            resourceInputs["endDate"] = undefined /*out*/;
            resourceInputs["endDateType"] = undefined /*out*/;
            resourceInputs["ephemeralStorage"] = undefined /*out*/;
            resourceInputs["instanceCount"] = undefined /*out*/;
            resourceInputs["instanceMatchCriteria"] = undefined /*out*/;
            resourceInputs["instancePlatform"] = undefined /*out*/;
            resourceInputs["instanceType"] = undefined /*out*/;
            resourceInputs["outPostArn"] = undefined /*out*/;
            resourceInputs["placementGroupArn"] = undefined /*out*/;
            resourceInputs["tagSpecifications"] = undefined /*out*/;
            resourceInputs["tenancy"] = undefined /*out*/;
            resourceInputs["totalInstanceCount"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["availabilityZone", "ebsOptimized", "ephemeralStorage", "instanceMatchCriteria", "instancePlatform", "instanceType", "outPostArn", "placementGroupArn", "tagSpecifications[*]", "tenancy"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(CapacityReservation.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a CapacityReservation resource.
 */
export interface CapacityReservationArgs {
    availabilityZone: pulumi.Input<string>;
    ebsOptimized?: pulumi.Input<boolean>;
    endDate?: pulumi.Input<string>;
    endDateType?: pulumi.Input<string>;
    ephemeralStorage?: pulumi.Input<boolean>;
    instanceCount: pulumi.Input<number>;
    instanceMatchCriteria?: pulumi.Input<string>;
    instancePlatform: pulumi.Input<string>;
    instanceType: pulumi.Input<string>;
    outPostArn?: pulumi.Input<string>;
    placementGroupArn?: pulumi.Input<string>;
    tagSpecifications?: pulumi.Input<pulumi.Input<inputs.ec2.CapacityReservationTagSpecificationArgs>[]>;
    tenancy?: pulumi.Input<string>;
}
