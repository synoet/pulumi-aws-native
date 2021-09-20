// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    /// <summary>
    /// &lt;p&gt;A version of a theme.&lt;/p&gt;
    /// </summary>
    [OutputType]
    public sealed class ThemeThemeVersion
    {
        /// <summary>
        /// &lt;p&gt;The Amazon Resource Name (ARN) of the resource.&lt;/p&gt;
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// &lt;p&gt;The Amazon QuickSight-defined ID of the theme that a custom theme inherits from. All
        ///             themes initially inherit from a default QuickSight theme.&lt;/p&gt;
        /// </summary>
        public readonly string? BaseThemeId;
        public readonly Outputs.ThemeThemeConfiguration? Configuration;
        /// <summary>
        /// &lt;p&gt;The date and time that this theme version was created.&lt;/p&gt;
        /// </summary>
        public readonly string? CreatedTime;
        /// <summary>
        /// &lt;p&gt;The description of the theme.&lt;/p&gt;
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// &lt;p&gt;Errors associated with the theme.&lt;/p&gt;
        /// </summary>
        public readonly ImmutableArray<Outputs.ThemeThemeError> Errors;
        public readonly Pulumi.AwsNative.QuickSight.ThemeResourceStatus? Status;
        /// <summary>
        /// &lt;p&gt;The version number of the theme.&lt;/p&gt;
        /// </summary>
        public readonly double? VersionNumber;

        [OutputConstructor]
        private ThemeThemeVersion(
            string? arn,

            string? baseThemeId,

            Outputs.ThemeThemeConfiguration? configuration,

            string? createdTime,

            string? description,

            ImmutableArray<Outputs.ThemeThemeError> errors,

            Pulumi.AwsNative.QuickSight.ThemeResourceStatus? status,

            double? versionNumber)
        {
            Arn = arn;
            BaseThemeId = baseThemeId;
            Configuration = configuration;
            CreatedTime = createdTime;
            Description = description;
            Errors = errors;
            Status = status;
            VersionNumber = versionNumber;
        }
    }
}
