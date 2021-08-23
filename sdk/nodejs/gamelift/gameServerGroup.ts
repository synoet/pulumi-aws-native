// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html
 */
export class GameServerGroup extends pulumi.CustomResource {
    /**
     * Get an existing GameServerGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): GameServerGroup {
        return new GameServerGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:gamelift:GameServerGroup';

    /**
     * Returns true if the given object is an instance of GameServerGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GameServerGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GameServerGroup.__pulumiType;
    }

    public /*out*/ readonly autoScalingGroupArn!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-autoscalingpolicy
     */
    public readonly autoScalingPolicy!: pulumi.Output<outputs.gamelift.GameServerGroupAutoScalingPolicy | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-balancingstrategy
     */
    public readonly balancingStrategy!: pulumi.Output<string | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-deleteoption
     */
    public readonly deleteOption!: pulumi.Output<string | undefined>;
    public /*out*/ readonly gameServerGroupArn!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-gameservergroupname
     */
    public readonly gameServerGroupName!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-gameserverprotectionpolicy
     */
    public readonly gameServerProtectionPolicy!: pulumi.Output<string | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-instancedefinitions
     */
    public readonly instanceDefinitions!: pulumi.Output<outputs.gamelift.GameServerGroupInstanceDefinition[]>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-launchtemplate
     */
    public readonly launchTemplate!: pulumi.Output<outputs.gamelift.GameServerGroupLaunchTemplate>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-maxsize
     */
    public readonly maxSize!: pulumi.Output<number | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-minsize
     */
    public readonly minSize!: pulumi.Output<number | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-rolearn
     */
    public readonly roleArn!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-tags
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-vpcsubnets
     */
    public readonly vpcSubnets!: pulumi.Output<string[] | undefined>;

    /**
     * Create a GameServerGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GameServerGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.gameServerGroupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'gameServerGroupName'");
            }
            if ((!args || args.instanceDefinitions === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceDefinitions'");
            }
            if ((!args || args.launchTemplate === undefined) && !opts.urn) {
                throw new Error("Missing required property 'launchTemplate'");
            }
            if ((!args || args.roleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roleArn'");
            }
            inputs["autoScalingPolicy"] = args ? args.autoScalingPolicy : undefined;
            inputs["balancingStrategy"] = args ? args.balancingStrategy : undefined;
            inputs["deleteOption"] = args ? args.deleteOption : undefined;
            inputs["gameServerGroupName"] = args ? args.gameServerGroupName : undefined;
            inputs["gameServerProtectionPolicy"] = args ? args.gameServerProtectionPolicy : undefined;
            inputs["instanceDefinitions"] = args ? args.instanceDefinitions : undefined;
            inputs["launchTemplate"] = args ? args.launchTemplate : undefined;
            inputs["maxSize"] = args ? args.maxSize : undefined;
            inputs["minSize"] = args ? args.minSize : undefined;
            inputs["roleArn"] = args ? args.roleArn : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["vpcSubnets"] = args ? args.vpcSubnets : undefined;
            inputs["autoScalingGroupArn"] = undefined /*out*/;
            inputs["gameServerGroupArn"] = undefined /*out*/;
        } else {
            inputs["autoScalingGroupArn"] = undefined /*out*/;
            inputs["autoScalingPolicy"] = undefined /*out*/;
            inputs["balancingStrategy"] = undefined /*out*/;
            inputs["deleteOption"] = undefined /*out*/;
            inputs["gameServerGroupArn"] = undefined /*out*/;
            inputs["gameServerGroupName"] = undefined /*out*/;
            inputs["gameServerProtectionPolicy"] = undefined /*out*/;
            inputs["instanceDefinitions"] = undefined /*out*/;
            inputs["launchTemplate"] = undefined /*out*/;
            inputs["maxSize"] = undefined /*out*/;
            inputs["minSize"] = undefined /*out*/;
            inputs["roleArn"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["vpcSubnets"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(GameServerGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a GameServerGroup resource.
 */
export interface GameServerGroupArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-autoscalingpolicy
     */
    autoScalingPolicy?: pulumi.Input<inputs.gamelift.GameServerGroupAutoScalingPolicyArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-balancingstrategy
     */
    balancingStrategy?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-deleteoption
     */
    deleteOption?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-gameservergroupname
     */
    gameServerGroupName: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-gameserverprotectionpolicy
     */
    gameServerProtectionPolicy?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-instancedefinitions
     */
    instanceDefinitions: pulumi.Input<pulumi.Input<inputs.gamelift.GameServerGroupInstanceDefinitionArgs>[]>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-launchtemplate
     */
    launchTemplate: pulumi.Input<inputs.gamelift.GameServerGroupLaunchTemplateArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-maxsize
     */
    maxSize?: pulumi.Input<number>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-minsize
     */
    minSize?: pulumi.Input<number>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-rolearn
     */
    roleArn: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-tags
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-vpcsubnets
     */
    vpcSubnets?: pulumi.Input<pulumi.Input<string>[]>;
}
