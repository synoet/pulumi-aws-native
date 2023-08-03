// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Rds.Outputs
{

    [OutputType]
    public sealed class DbProxyTargetGroupConnectionPoolConfigurationInfoFormat
    {
        /// <summary>
        /// The number of seconds for a proxy to wait for a connection to become available in the connection pool.
        /// </summary>
        public readonly int? ConnectionBorrowTimeout;
        /// <summary>
        /// One or more SQL statements for the proxy to run when opening each new database connection.
        /// </summary>
        public readonly string? InitQuery;
        /// <summary>
        /// The maximum size of the connection pool for each target in a target group.
        /// </summary>
        public readonly int? MaxConnectionsPercent;
        /// <summary>
        /// Controls how actively the proxy closes idle database connections in the connection pool.
        /// </summary>
        public readonly int? MaxIdleConnectionsPercent;
        /// <summary>
        /// Each item in the list represents a class of SQL operations that normally cause all later statements in a session using a proxy to be pinned to the same underlying database connection.
        /// </summary>
        public readonly ImmutableArray<string> SessionPinningFilters;

        [OutputConstructor]
        private DbProxyTargetGroupConnectionPoolConfigurationInfoFormat(
            int? connectionBorrowTimeout,

            string? initQuery,

            int? maxConnectionsPercent,

            int? maxIdleConnectionsPercent,

            ImmutableArray<string> sessionPinningFilters)
        {
            ConnectionBorrowTimeout = connectionBorrowTimeout;
            InitQuery = initQuery;
            MaxConnectionsPercent = maxConnectionsPercent;
            MaxIdleConnectionsPercent = maxIdleConnectionsPercent;
            SessionPinningFilters = sessionPinningFilters;
        }
    }
}
