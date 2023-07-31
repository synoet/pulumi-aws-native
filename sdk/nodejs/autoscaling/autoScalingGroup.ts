// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AutoScaling::AutoScalingGroup
 *
 * @deprecated AutoScalingGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class AutoScalingGroup extends pulumi.CustomResource {
    /**
     * Get an existing AutoScalingGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AutoScalingGroup {
        pulumi.log.warn("AutoScalingGroup is deprecated: AutoScalingGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new AutoScalingGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:autoscaling:AutoScalingGroup';

    /**
     * Returns true if the given object is an instance of AutoScalingGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AutoScalingGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AutoScalingGroup.__pulumiType;
    }

    public readonly autoScalingGroupName!: pulumi.Output<string | undefined>;
    public readonly availabilityZones!: pulumi.Output<string[] | undefined>;
    public readonly capacityRebalance!: pulumi.Output<boolean | undefined>;
    public readonly context!: pulumi.Output<string | undefined>;
    public readonly cooldown!: pulumi.Output<string | undefined>;
    public readonly defaultInstanceWarmup!: pulumi.Output<number | undefined>;
    public readonly desiredCapacity!: pulumi.Output<string | undefined>;
    public readonly desiredCapacityType!: pulumi.Output<string | undefined>;
    public readonly healthCheckGracePeriod!: pulumi.Output<number | undefined>;
    public readonly healthCheckType!: pulumi.Output<string | undefined>;
    public readonly instanceId!: pulumi.Output<string | undefined>;
    public readonly launchConfigurationName!: pulumi.Output<string | undefined>;
    public readonly launchTemplate!: pulumi.Output<outputs.autoscaling.AutoScalingGroupLaunchTemplateSpecification | undefined>;
    public /*out*/ readonly launchTemplateSpecification!: pulumi.Output<string>;
    public readonly lifecycleHookSpecificationList!: pulumi.Output<outputs.autoscaling.AutoScalingGroupLifecycleHookSpecification[] | undefined>;
    public readonly loadBalancerNames!: pulumi.Output<string[] | undefined>;
    public readonly maxInstanceLifetime!: pulumi.Output<number | undefined>;
    public readonly maxSize!: pulumi.Output<string>;
    public readonly metricsCollection!: pulumi.Output<outputs.autoscaling.AutoScalingGroupMetricsCollection[] | undefined>;
    public readonly minSize!: pulumi.Output<string>;
    public readonly mixedInstancesPolicy!: pulumi.Output<outputs.autoscaling.AutoScalingGroupMixedInstancesPolicy | undefined>;
    public readonly newInstancesProtectedFromScaleIn!: pulumi.Output<boolean | undefined>;
    public readonly notificationConfigurations!: pulumi.Output<outputs.autoscaling.AutoScalingGroupNotificationConfiguration[] | undefined>;
    public readonly placementGroup!: pulumi.Output<string | undefined>;
    public readonly serviceLinkedRoleArn!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.autoscaling.AutoScalingGroupTagProperty[] | undefined>;
    public readonly targetGroupArns!: pulumi.Output<string[] | undefined>;
    public readonly terminationPolicies!: pulumi.Output<string[] | undefined>;
    public readonly vpcZoneIdentifier!: pulumi.Output<string[] | undefined>;

    /**
     * Create a AutoScalingGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated AutoScalingGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: AutoScalingGroupArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("AutoScalingGroup is deprecated: AutoScalingGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.maxSize === undefined) && !opts.urn) {
                throw new Error("Missing required property 'maxSize'");
            }
            if ((!args || args.minSize === undefined) && !opts.urn) {
                throw new Error("Missing required property 'minSize'");
            }
            resourceInputs["autoScalingGroupName"] = args ? args.autoScalingGroupName : undefined;
            resourceInputs["availabilityZones"] = args ? args.availabilityZones : undefined;
            resourceInputs["capacityRebalance"] = args ? args.capacityRebalance : undefined;
            resourceInputs["context"] = args ? args.context : undefined;
            resourceInputs["cooldown"] = args ? args.cooldown : undefined;
            resourceInputs["defaultInstanceWarmup"] = args ? args.defaultInstanceWarmup : undefined;
            resourceInputs["desiredCapacity"] = args ? args.desiredCapacity : undefined;
            resourceInputs["desiredCapacityType"] = args ? args.desiredCapacityType : undefined;
            resourceInputs["healthCheckGracePeriod"] = args ? args.healthCheckGracePeriod : undefined;
            resourceInputs["healthCheckType"] = args ? args.healthCheckType : undefined;
            resourceInputs["instanceId"] = args ? args.instanceId : undefined;
            resourceInputs["launchConfigurationName"] = args ? args.launchConfigurationName : undefined;
            resourceInputs["launchTemplate"] = args ? args.launchTemplate : undefined;
            resourceInputs["lifecycleHookSpecificationList"] = args ? args.lifecycleHookSpecificationList : undefined;
            resourceInputs["loadBalancerNames"] = args ? args.loadBalancerNames : undefined;
            resourceInputs["maxInstanceLifetime"] = args ? args.maxInstanceLifetime : undefined;
            resourceInputs["maxSize"] = args ? args.maxSize : undefined;
            resourceInputs["metricsCollection"] = args ? args.metricsCollection : undefined;
            resourceInputs["minSize"] = args ? args.minSize : undefined;
            resourceInputs["mixedInstancesPolicy"] = args ? args.mixedInstancesPolicy : undefined;
            resourceInputs["newInstancesProtectedFromScaleIn"] = args ? args.newInstancesProtectedFromScaleIn : undefined;
            resourceInputs["notificationConfigurations"] = args ? args.notificationConfigurations : undefined;
            resourceInputs["placementGroup"] = args ? args.placementGroup : undefined;
            resourceInputs["serviceLinkedRoleArn"] = args ? args.serviceLinkedRoleArn : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["targetGroupArns"] = args ? args.targetGroupArns : undefined;
            resourceInputs["terminationPolicies"] = args ? args.terminationPolicies : undefined;
            resourceInputs["vpcZoneIdentifier"] = args ? args.vpcZoneIdentifier : undefined;
            resourceInputs["launchTemplateSpecification"] = undefined /*out*/;
        } else {
            resourceInputs["autoScalingGroupName"] = undefined /*out*/;
            resourceInputs["availabilityZones"] = undefined /*out*/;
            resourceInputs["capacityRebalance"] = undefined /*out*/;
            resourceInputs["context"] = undefined /*out*/;
            resourceInputs["cooldown"] = undefined /*out*/;
            resourceInputs["defaultInstanceWarmup"] = undefined /*out*/;
            resourceInputs["desiredCapacity"] = undefined /*out*/;
            resourceInputs["desiredCapacityType"] = undefined /*out*/;
            resourceInputs["healthCheckGracePeriod"] = undefined /*out*/;
            resourceInputs["healthCheckType"] = undefined /*out*/;
            resourceInputs["instanceId"] = undefined /*out*/;
            resourceInputs["launchConfigurationName"] = undefined /*out*/;
            resourceInputs["launchTemplate"] = undefined /*out*/;
            resourceInputs["launchTemplateSpecification"] = undefined /*out*/;
            resourceInputs["lifecycleHookSpecificationList"] = undefined /*out*/;
            resourceInputs["loadBalancerNames"] = undefined /*out*/;
            resourceInputs["maxInstanceLifetime"] = undefined /*out*/;
            resourceInputs["maxSize"] = undefined /*out*/;
            resourceInputs["metricsCollection"] = undefined /*out*/;
            resourceInputs["minSize"] = undefined /*out*/;
            resourceInputs["mixedInstancesPolicy"] = undefined /*out*/;
            resourceInputs["newInstancesProtectedFromScaleIn"] = undefined /*out*/;
            resourceInputs["notificationConfigurations"] = undefined /*out*/;
            resourceInputs["placementGroup"] = undefined /*out*/;
            resourceInputs["serviceLinkedRoleArn"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["targetGroupArns"] = undefined /*out*/;
            resourceInputs["terminationPolicies"] = undefined /*out*/;
            resourceInputs["vpcZoneIdentifier"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AutoScalingGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a AutoScalingGroup resource.
 */
export interface AutoScalingGroupArgs {
    autoScalingGroupName?: pulumi.Input<string>;
    availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
    capacityRebalance?: pulumi.Input<boolean>;
    context?: pulumi.Input<string>;
    cooldown?: pulumi.Input<string>;
    defaultInstanceWarmup?: pulumi.Input<number>;
    desiredCapacity?: pulumi.Input<string>;
    desiredCapacityType?: pulumi.Input<string>;
    healthCheckGracePeriod?: pulumi.Input<number>;
    healthCheckType?: pulumi.Input<string>;
    instanceId?: pulumi.Input<string>;
    launchConfigurationName?: pulumi.Input<string>;
    launchTemplate?: pulumi.Input<inputs.autoscaling.AutoScalingGroupLaunchTemplateSpecificationArgs>;
    lifecycleHookSpecificationList?: pulumi.Input<pulumi.Input<inputs.autoscaling.AutoScalingGroupLifecycleHookSpecificationArgs>[]>;
    loadBalancerNames?: pulumi.Input<pulumi.Input<string>[]>;
    maxInstanceLifetime?: pulumi.Input<number>;
    maxSize: pulumi.Input<string>;
    metricsCollection?: pulumi.Input<pulumi.Input<inputs.autoscaling.AutoScalingGroupMetricsCollectionArgs>[]>;
    minSize: pulumi.Input<string>;
    mixedInstancesPolicy?: pulumi.Input<inputs.autoscaling.AutoScalingGroupMixedInstancesPolicyArgs>;
    newInstancesProtectedFromScaleIn?: pulumi.Input<boolean>;
    notificationConfigurations?: pulumi.Input<pulumi.Input<inputs.autoscaling.AutoScalingGroupNotificationConfigurationArgs>[]>;
    placementGroup?: pulumi.Input<string>;
    serviceLinkedRoleArn?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.autoscaling.AutoScalingGroupTagPropertyArgs>[]>;
    targetGroupArns?: pulumi.Input<pulumi.Input<string>[]>;
    terminationPolicies?: pulumi.Input<pulumi.Input<string>[]>;
    vpcZoneIdentifier?: pulumi.Input<pulumi.Input<string>[]>;
}
