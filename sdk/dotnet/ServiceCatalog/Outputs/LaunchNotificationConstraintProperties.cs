// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.ServiceCatalog.Outputs
{

    [OutputType]
    public sealed class LaunchNotificationConstraintProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-acceptlanguage
        /// </summary>
        public readonly string? AcceptLanguage;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-description
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-notificationarns
        /// </summary>
        public readonly ImmutableArray<string> NotificationArns;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-portfolioid
        /// </summary>
        public readonly string PortfolioId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-productid
        /// </summary>
        public readonly string ProductId;

        [OutputConstructor]
        private LaunchNotificationConstraintProperties(
            string? AcceptLanguage,

            string? Description,

            ImmutableArray<string> NotificationArns,

            string PortfolioId,

            string ProductId)
        {
            this.AcceptLanguage = AcceptLanguage;
            this.Description = Description;
            this.NotificationArns = NotificationArns;
            this.PortfolioId = PortfolioId;
            this.ProductId = ProductId;
        }
    }
}