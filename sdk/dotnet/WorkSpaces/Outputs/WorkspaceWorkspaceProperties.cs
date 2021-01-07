// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.WorkSpaces.Outputs
{

    [OutputType]
    public sealed class WorkspaceWorkspaceProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-computetypename
        /// </summary>
        public readonly string? ComputeTypeName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-rootvolumesizegib
        /// </summary>
        public readonly int? RootVolumeSizeGib;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-runningmode
        /// </summary>
        public readonly string? RunningMode;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-runningmodeautostoptimeoutinminutes
        /// </summary>
        public readonly int? RunningModeAutoStopTimeoutInMinutes;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-uservolumesizegib
        /// </summary>
        public readonly int? UserVolumeSizeGib;

        [OutputConstructor]
        private WorkspaceWorkspaceProperties(
            string? ComputeTypeName,

            int? RootVolumeSizeGib,

            string? RunningMode,

            int? RunningModeAutoStopTimeoutInMinutes,

            int? UserVolumeSizeGib)
        {
            this.ComputeTypeName = ComputeTypeName;
            this.RootVolumeSizeGib = RootVolumeSizeGib;
            this.RunningMode = RunningMode;
            this.RunningModeAutoStopTimeoutInMinutes = RunningModeAutoStopTimeoutInMinutes;
            this.UserVolumeSizeGib = UserVolumeSizeGib;
        }
    }
}