// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CodeDeploy::DeploymentGroup
 */
export function getDeploymentGroup(args: GetDeploymentGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetDeploymentGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:codedeploy:getDeploymentGroup", {
        "id": args.id,
    }, opts);
}

export interface GetDeploymentGroupArgs {
    id: string;
}

export interface GetDeploymentGroupResult {
    readonly alarmConfiguration?: outputs.codedeploy.DeploymentGroupAlarmConfiguration;
    readonly autoRollbackConfiguration?: outputs.codedeploy.DeploymentGroupAutoRollbackConfiguration;
    readonly autoScalingGroups?: string[];
    readonly blueGreenDeploymentConfiguration?: outputs.codedeploy.DeploymentGroupBlueGreenDeploymentConfiguration;
    readonly deployment?: outputs.codedeploy.DeploymentGroupDeployment;
    readonly deploymentConfigName?: string;
    readonly deploymentStyle?: outputs.codedeploy.DeploymentGroupDeploymentStyle;
    readonly ec2TagFilters?: outputs.codedeploy.DeploymentGroupEc2TagFilter[];
    readonly ec2TagSet?: outputs.codedeploy.DeploymentGroupEc2TagSet;
    readonly ecsServices?: outputs.codedeploy.DeploymentGroupEcsService[];
    readonly id?: string;
    readonly loadBalancerInfo?: outputs.codedeploy.DeploymentGroupLoadBalancerInfo;
    readonly onPremisesInstanceTagFilters?: outputs.codedeploy.DeploymentGroupTagFilter[];
    readonly onPremisesTagSet?: outputs.codedeploy.DeploymentGroupOnPremisesTagSet;
    readonly outdatedInstancesStrategy?: string;
    readonly serviceRoleArn?: string;
    readonly tags?: outputs.codedeploy.DeploymentGroupTag[];
    readonly triggerConfigurations?: outputs.codedeploy.DeploymentGroupTriggerConfig[];
}
/**
 * Resource Type definition for AWS::CodeDeploy::DeploymentGroup
 */
export function getDeploymentGroupOutput(args: GetDeploymentGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDeploymentGroupResult> {
    return pulumi.output(args).apply((a: any) => getDeploymentGroup(a, opts))
}

export interface GetDeploymentGroupOutputArgs {
    id: pulumi.Input<string>;
}
